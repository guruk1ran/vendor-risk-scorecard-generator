package com.internship.tool.controller;

import com.internship.tool.entity.Scorecard;
import com.internship.tool.service.ScorecardService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/scorecards")
@RequiredArgsConstructor
public class ScorecardController {

    private final ScorecardService scorecardService;

    @GetMapping
    public ResponseEntity<List<Scorecard>> getAllScorecards() {
        return ResponseEntity.ok(scorecardService.getAllScorecards());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Scorecard> getScorecardById(@PathVariable Long id) {
        return ResponseEntity.ok(scorecardService.getScorecardById(id));
    }

    @GetMapping("/vendor/{vendorId}")
    public ResponseEntity<List<Scorecard>> getScorecardsByVendor(@PathVariable Long vendorId) {
        return ResponseEntity.ok(scorecardService.getScorecardsByVendor(vendorId));
    }

    @PreAuthorize("hasRole('ADMIN')")
    @PostMapping("/vendor/{vendorId}")
    public ResponseEntity<Scorecard> createScorecard(
            @PathVariable Long vendorId,
            @RequestBody Scorecard scorecard) {
        Scorecard createdScorecard = scorecardService.createScorecard(vendorId, scorecard);
        return new ResponseEntity<>(createdScorecard, HttpStatus.CREATED);
    }

    @PreAuthorize("hasRole('ADMIN')")
    @PutMapping("/{id}")
    public ResponseEntity<Scorecard> updateScorecard(
            @PathVariable Long id,
            @RequestBody Scorecard scorecard) {
        return ResponseEntity.ok(scorecardService.updateScorecard(id, scorecard));
    }

    @PreAuthorize("hasRole('ADMIN')")
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteScorecard(@PathVariable Long id) {
        scorecardService.deleteScorecard(id);
        return ResponseEntity.noContent().build();
    }
}
