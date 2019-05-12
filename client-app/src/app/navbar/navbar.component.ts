import { Component, OnInit } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { Laptop } from '../laptop/models/laptop';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  public laptop: Laptop;

  constructor(
    public laptopService: LaptopService
  ) { }

  ngOnInit() {
  }

  checkResult() {
    return this.laptopService.getLaptopFromCookie() !== null;
  }

}
