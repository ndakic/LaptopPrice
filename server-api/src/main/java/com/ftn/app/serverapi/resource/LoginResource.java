package com.ftn.app.serverapi.resource;

import lombok.*;

@Getter
@Setter
@ToString
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class LoginResource{

    private String username;
    private String password;
}
