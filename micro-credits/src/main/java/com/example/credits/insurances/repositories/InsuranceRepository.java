package com.example.credits.insurances.repositories;

import com.example.credits.insurances.entities.InsuranceEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface InsuranceRepository extends JpaRepository<InsuranceEntity, Long> {
}
