package com.internship.tool.repository;

import com.internship.tool.entity.Scorecard;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ScorecardRepository extends JpaRepository<Scorecard, Long> {
    List<Scorecard> findByVendorId(Long vendorId);
}
