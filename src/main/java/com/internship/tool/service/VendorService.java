package com.internship.tool.service;

import com.internship.tool.entity.Vendor;
import com.internship.tool.exception.ResourceNotFoundException;
import com.internship.tool.repository.VendorRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class VendorService {

    private final VendorRepository vendorRepository;

    @Cacheable(value = "vendors")
    public List<Vendor> getAllVendors() {
        return vendorRepository.findAll();
    }

    @Cacheable(value = "vendor", key = "#id")
    public Vendor getVendorById(Long id) {
        return vendorRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Vendor not found with id: " + id));
    }

    @CacheEvict(value = "vendors", allEntries = true)
    public Vendor createVendor(Vendor vendor) {
        return vendorRepository.save(vendor);
    }

    @CacheEvict(value = {"vendors", "vendor"}, allEntries = true)
    public Vendor updateVendor(Long id, Vendor vendorDetails) {
        Vendor vendor = getVendorById(id);
        vendor.setName(vendorDetails.getName());
        vendor.setContactEmail(vendorDetails.getContactEmail());
        vendor.setIndustry(vendorDetails.getIndustry());
        return vendorRepository.save(vendor);
    }

    @CacheEvict(value = {"vendors", "vendor"}, allEntries = true)
    public void deleteVendor(Long id) {
        Vendor vendor = getVendorById(id);
        vendorRepository.delete(vendor);
    }
}
