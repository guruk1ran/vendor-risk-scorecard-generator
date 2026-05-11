package com.internship.tool.service;

import com.internship.tool.entity.Vendor;
import com.internship.tool.exception.ResourceNotFoundException;
import com.internship.tool.repository.VendorRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class VendorServiceTest {

    @Mock
    private VendorRepository vendorRepository;

    @InjectMocks
    private VendorService vendorService;

    private Vendor vendor;

    @BeforeEach
    void setUp() {
        vendor = Vendor.builder()
                .id(1L)
                .name("Test Vendor")
                .contactEmail("test@test.com")
                .industry("IT")
                .build();
    }

    @Test
    void testGetVendorById_Success() {
        when(vendorRepository.findById(1L)).thenReturn(Optional.of(vendor));

        Vendor result = vendorService.getVendorById(1L);

        assertNotNull(result);
        assertEquals("Test Vendor", result.getName());
        verify(vendorRepository, times(1)).findById(1L);
    }

    @Test
    void testGetVendorById_NotFound() {
        when(vendorRepository.findById(1L)).thenReturn(Optional.empty());

        assertThrows(ResourceNotFoundException.class, () -> {
            vendorService.getVendorById(1L);
        });
        verify(vendorRepository, times(1)).findById(1L);
    }

    @Test
    void testCreateVendor() {
        when(vendorRepository.save(any(Vendor.class))).thenReturn(vendor);

        Vendor result = vendorService.createVendor(vendor);

        assertNotNull(result);
        assertEquals("Test Vendor", result.getName());
        verify(vendorRepository, times(1)).save(any(Vendor.class));
    }
}
