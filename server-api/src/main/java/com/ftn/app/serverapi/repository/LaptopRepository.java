package com.ftn.app.serverapi.repository;

import com.ftn.app.serverapi.model.Laptop;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface LaptopRepository extends JpaRepository<Laptop, Long> {

    Optional<Laptop> getOneById(Long id);

    List<Laptop> findAllByOrderByPriceDesc();

    List<Laptop> findByBrandIgnoreCaseContaining(String brand);

    @Query(value = "SELECT l from Laptop l where price > :lbound and price < :ubound and condition = :condition")
    List<Laptop> findAllByPriceBoundsAndCondition(@Param("lbound") Integer lbound, @Param("ubound") Integer ubound, @Param("condition") String condition);

    @Query(value = "SELECT DISTINCT brand from Laptop WHERE brand <> '' order by brand asc")
    List<String> findAllLaptopBrands();

    @Query(value = "SELECT DISTINCT processorBrand from Laptop WHERE processorBrand <> '' order by processorBrand asc")
    List<String> findAllLaptopProcessorBrands();

    @Query(value = "SELECT DISTINCT processorModel from Laptop WHERE processorModel <> '' order by processorModel asc")
    List<String> findAllLaptopProcessorModels();

    @Query(value = "SELECT DISTINCT cores from Laptop WHERE cores <> '' order by cores asc")
    List<String> findAllLaptopCores();

    @Query(value = "SELECT DISTINCT ramGeneration from Laptop WHERE ramGeneration <> '' order by ramGeneration asc")
    List<String> findAllLaptopRamGenerations();

    @Query(value = "SELECT DISTINCT ramAmount from Laptop order by ramAmount asc")
    List<String> findAllLaptopRamAmounts();

    @Query(value = "SELECT DISTINCT storageType from Laptop WHERE storageType <> '' order by storageType asc")
    List<String> findAllLaptopStorageTypes();

    @Query(value = "SELECT DISTINCT storageAmount from Laptop order by storageAmount asc")
    List<String> findAllLaptopStorageAmounts();

    @Query(value = "SELECT DISTINCT screenSize from Laptop WHERE screenSize <> '' order by screenSize asc")
    List<String> findAllLaptopScreenSizes();

    @Query(value = "SELECT DISTINCT condition from Laptop WHERE condition <> '' order by condition asc")
    List<String> findAllLaptopConditions();

}
