package com.ftn.app.serverapi.model;

import lombok.*;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "scraper")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class Scraper {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "scraper_generator")
    @SequenceGenerator(name="scraper_generator", sequenceName = "scraper_seq")
    private Long id;

    private String source;
    private Date date;
    private String total;
    private String status;

}

