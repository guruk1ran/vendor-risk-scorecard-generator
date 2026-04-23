package com.internship.tool.service;

import com.internship.tool.entity.Scorecard;
import com.internship.tool.entity.Vendor;
import com.internship.tool.exception.ResourceNotFoundException;
import com.internship.tool.repository.ScorecardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ScorecardService {

    private final ScorecardRepository scorecardRepository;
    private final VendorService vendorService;

    @Cacheable(value = "scorecards")
    public List<Scorecard> getAllScorecards() {
        return scorecardRepository.findAll();
    }

    @Cacheable(value = "scorecard", key = "#id")
    public Scorecard getScorecardById(Long id) {
        return scorecardRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Scorecard not found with id: " + id));
    }

    @Cacheable(value = "scorecardsByVendor", key = "#vendorId")
    public List<Scorecard> getScorecardsByVendor(Long vendorId) {
        // verify vendor exists
        vendorService.getVendorById(vendorId);
        return scorecardRepository.findByVendorId(vendorId);
    }

    @CacheEvict(value = {"scorecards", "scorecardsByVendor"}, allEntries = true)
    public Scorecard createScorecard(Long vendorId, Scorecard scorecard) {
        Vendor vendor = vendorService.getVendorById(vendorId);
        scorecard.setVendor(vendor);
        return scorecardRepository.save(scorecard);
    }

    @CacheEvict(value = {"scorecards", "scorecard", "scorecardsByVendor"}, allEntries = true)
    public Scorecard updateScorecard(Long id, Scorecard scorecardDetails) {
        Scorecard scorecard = getScorecardById(id);
        scorecard.setScore(scorecardDetails.getScore());
        scorecard.setRiskLevel(scorecardDetails.getRiskLevel());
        return scorecardRepository.save(scorecard);
    }

    @CacheEvict(value = {"scorecards", "scorecard", "scorecardsByVendor"}, allEntries = true)
    public void deleteScorecard(Long id) {
        Scorecard scorecard = getScorecardById(id);
        scorecardRepository.delete(scorecard);
    }
}
