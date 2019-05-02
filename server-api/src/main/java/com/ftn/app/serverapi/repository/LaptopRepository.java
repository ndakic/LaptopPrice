package com.ftn.app.serverapi.repository;

import com.ftn.app.serverapi.model.Laptop;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface LaptopRepository extends JpaRepository<Laptop, Long> {

    Optional<Laptop> getOneById(Long id);

    List<Laptop> findAllByOrderByPriceDesc();

    @Query(value = "SELECT DISTINCT brand from Laptop")
    List<String> findAllLaptopBrands();

    @Query(value = "SELECT DISTINCT processorBrand from Laptop")
    List<String> findAllLaptopProcessorBrands();

    @Query(value = "SELECT DISTINCT processorModel from Laptop")
    List<String> findAllLaptopProcessorModels();

    @Query(value = "SELECT DISTINCT cores from Laptop")
    List<String> findAllLaptopCores();

    @Query(value = "SELECT DISTINCT ramGeneration from Laptop")
    List<String> findAllLaptopRamGenerations();

    @Query(value = "SELECT DISTINCT ramAmount from Laptop")
    List<String> findAllLaptopRamAmounts();

    @Query(value = "SELECT DISTINCT storageType from Laptop")
    List<String> findAllLaptopStorageTypes();

    @Query(value = "SELECT DISTINCT storageAmount from Laptop")
    List<String> findAllLaptopStorageAmounts();

    @Query(value = "SELECT DISTINCT screenSize from Laptop")
    List<String> findAllLaptopScreenSizes();

    @Query(value = "SELECT DISTINCT condition from Laptop")
    List<String> findAllLaptopConditions();

}
