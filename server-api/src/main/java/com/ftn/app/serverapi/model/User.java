package com.ftn.app.serverapi.model;

import lombok.*;
import javax.persistence.*;

@Entity
@Table(name = "users")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Long id;
    @Column(unique=true)
    private String username;
    @Column(nullable = false)
    private String password;
    @Column(unique=true)
    private String email;
    private String firstName;
    private String lastName;
}
