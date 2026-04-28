package com.internship.tool.service;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import com.internship.tool.repository.ScorecardRepository;

import static org.junit.jupiter.api.Assertions.assertNotNull;

@ExtendWith(MockitoExtension.class)
public class ScorecardServiceTest {

    @Mock
    private ScorecardRepository scorecardRepository;

    @Mock
    private VendorService vendorService;

    @InjectMocks
    private ScorecardService scorecardService;

    @Test
    void testServiceNotNull() {
        assertNotNull(scorecardService);
    }
}
