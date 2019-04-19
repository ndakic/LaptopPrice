import { Component, OnInit } from '@angular/core';
import { LaptopService } from './services/laptop.service';

@Component({
  selector: 'app-laptop',
  templateUrl: './laptop.component.html',
  styleUrls: ['./laptop.component.css']
})
export class LaptopComponent implements OnInit {

  public laptops: any;

  constructor(public laptopService: LaptopService) { }

  ngOnInit() {

    this.laptopService.getLaptops().subscribe(laptops => this.laptops = laptops);
  }

}
