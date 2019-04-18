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

    public List<Laptop> getAllLaptops(){
        return laptopRepository.findAll();
    }
}
