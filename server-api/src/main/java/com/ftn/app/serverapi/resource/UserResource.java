package com.ftn.app.serverapi.resource;


import lombok.*;

@ToString
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class UserResource {

    private String username;
    private String password;
    private String email;
    private String firstName;
    private String lastName;

}
