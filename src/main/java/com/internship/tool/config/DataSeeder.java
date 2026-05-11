package com.internship.tool.config;

import com.internship.tool.entity.RiskLevel;
import com.internship.tool.entity.Role;
import com.internship.tool.entity.Scorecard;
import com.internship.tool.entity.User;
import com.internship.tool.entity.Vendor;
import com.internship.tool.repository.ScorecardRepository;
import com.internship.tool.repository.UserRepository;
import com.internship.tool.repository.VendorRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;

@Component
@RequiredArgsConstructor
public class DataSeeder implements CommandLineRunner {

    private final UserRepository userRepository;
    private final VendorRepository vendorRepository;
    private final ScorecardRepository scorecardRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public void run(String... args) throws Exception {
        if (userRepository.count() == 0) {
            User admin = User.builder()
                    .username("admin")
                    .password(passwordEncoder.encode("admin123"))
                    .role(Role.ADMIN)
                    .build();
            userRepository.save(admin);
            
            User user = User.builder()
                    .username("user")
                    .password(passwordEncoder.encode("user123"))
                    .role(Role.USER)
                    .build();
            userRepository.save(user);
            System.out.println("Demo users seeded.");
        }

        if (vendorRepository.count() == 0) {
            Vendor vendor1 = Vendor.builder()
                    .name("TechCorp Inc.")
                    .contactEmail("contact@techcorp.com")
                    .industry("Technology")
                    .build();
            vendor1 = vendorRepository.save(vendor1);

            Vendor vendor2 = Vendor.builder()
                    .name("SecureFinance LLC")
                    .contactEmail("info@securefinance.com")
                    .industry("Finance")
                    .build();
            vendor2 = vendorRepository.save(vendor2);
            System.out.println("Demo vendors seeded.");

            if (scorecardRepository.count() == 0) {
                Scorecard scorecard1 = Scorecard.builder()
                        .vendor(vendor1)
                        .score(85)
                        .riskLevel(RiskLevel.LOW)
                        .evaluationDate(LocalDateTime.now().minusDays(10))
                        .build();
                scorecardRepository.save(scorecard1);

                Scorecard scorecard2 = Scorecard.builder()
                        .vendor(vendor2)
                        .score(45)
                        .riskLevel(RiskLevel.HIGH)
                        .evaluationDate(LocalDateTime.now().minusDays(2))
                        .build();
                scorecardRepository.save(scorecard2);
                System.out.println("Demo scorecards seeded.");
            }
        }
    }
}
