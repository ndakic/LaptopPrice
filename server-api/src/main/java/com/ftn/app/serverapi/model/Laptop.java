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
    private Long id;
    private String brand;
    private String processorBrand;
    private String processorModel;
    private String cores;
    private String ramGeneration;
    private Integer ramAmount;
    private String storageType;
    private Integer storageAmount;
    private String screenSize;
    private Integer price;
    private String condition;
    private String url;

}
