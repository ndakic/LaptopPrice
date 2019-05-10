package com.ftn.app.serverapi.service;

import com.ftn.app.serverapi.model.Laptop;
import com.ftn.app.serverapi.repository.LaptopRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class LaptopService {

    private LaptopRepository laptopRepository;


    public Laptop saveLaptop(Laptop laptop){
       return laptopRepository.save(laptop);
    }

    public Laptop getLaptop(Long id){
        return laptopRepository.getOneById(id).orElse(null);
    }

    public List<Laptop> searchLaptopsByBrand(String term) {
        return laptopRepository.findByBrandIgnoreCaseContaining(term);
    }

    public List<Laptop> getAllLaptops(){
        return laptopRepository.findAllByOrderByPriceDesc();
    }

    public List<String> getAllLaptopBrands(){
        return laptopRepository.findAllLaptopBrands();
    }

    public List<String> getAllLaptopProcessorBrands(){
        return laptopRepository.findAllLaptopProcessorBrands();
    }

    public List<String> getAllLaptopProcessorModels(){
        return laptopRepository.findAllLaptopProcessorModels();
    }

    public List<String> getAllLaptopCores(){
        return laptopRepository.findAllLaptopCores();
    }

    public List<String> getAllLaptopRamGenerations(){
        return laptopRepository.findAllLaptopRamGenerations();
    }

    public List<String> getAllLaptopRamAmounts(){
        return laptopRepository.findAllLaptopRamAmounts();
    }

    public List<String> getAllLaptopStorageTypes(){
        return laptopRepository.findAllLaptopStorageTypes();
    }

    public List<String> getAllLaptopStorageAmounts(){
        return laptopRepository.findAllLaptopStorageAmounts();
    }

    public List<String> getAllLaptopScreenSizes(){
        return laptopRepository.findAllLaptopScreenSizes();
    }

    public List<String> getAllLaptopConditions(){
        return laptopRepository.findAllLaptopConditions();
    }
}
