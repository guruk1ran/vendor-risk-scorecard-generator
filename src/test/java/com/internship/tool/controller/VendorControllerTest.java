package com.internship.tool.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;

import com.internship.tool.service.VendorService;
import com.internship.tool.config.JwtAuthenticationFilter;
import org.springframework.security.authentication.AuthenticationProvider;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(VendorController.class)
public class VendorControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private VendorService vendorService;

    @MockBean
    private JwtAuthenticationFilter jwtAuthFilter;

    @MockBean
    private AuthenticationProvider authenticationProvider;

    @Test
    @WithMockUser
    void testGetVendors() throws Exception {
        mockMvc.perform(get("/api/vendors"))
                .andExpect(status().isOk());
    }
}
