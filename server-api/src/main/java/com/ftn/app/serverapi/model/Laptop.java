package com.ftn.app.serverapi.model;

import lombok.*;

import javax.persistence.*;

@Entity
@Table(name = "laptop")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class Laptop {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Long id;

    private String brand;
    private String product;
    private String processorBrand;
    private String processorModel;
    private Integer cores;
    private String ramGeneration;
    private Integer ramAmount;
    private String storageType;
    private Integer storageAmount;
    private Integer screenSize;
    private Integer price;

}
