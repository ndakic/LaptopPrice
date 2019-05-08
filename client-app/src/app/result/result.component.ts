import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { Laptop } from '../laptop/models/laptop';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  public laptop: Laptop;
  public laptopPrice: any;

  constructor(
    public laptopService: LaptopService
  ) {
    this.laptop = new Laptop();
   }

  ngOnInit() {
    this.laptopPrice = 0;

    if (this.laptopService.getLaptopSpecs()) {
      this.laptop = this.laptopService.getLaptopSpecs();
      this.laptopPrice = this.getLaptopPrice(this.laptop);
      localStorage.setItem('laptopSpecs', JSON.stringify(this.laptop));
      localStorage.setItem('laptopPrice', this.getLaptopPrice(this.laptop).toString());
    } else {
      if (localStorage.getItem('laptopSpecs') !== null) {
        this.laptop = JSON.parse(localStorage.getItem('laptopSpecs'));
        this.laptopPrice = localStorage.getItem('laptopPrice');
      }
    }
  }

  getLaptopPrice(laptop) {
    return Math.floor(Math.random() * 100) * 1000;
  }
}
