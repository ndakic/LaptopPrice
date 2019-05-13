import { Component, OnInit } from '@angular/core';
import { LaptopService } from './services/laptop.service';
import { NgBlockUI, BlockUI } from 'ng-block-ui';

@Component({
  selector: 'app-laptop',
  templateUrl: './laptop.component.html',
  styleUrls: ['./laptop.component.css']
})
export class LaptopComponent implements OnInit {

  @BlockUI() blockUI: NgBlockUI;

  public laptops: any;
  public scraperInfo: any;
  public brand: any;

  constructor(public laptopService: LaptopService) { }

  ngOnInit() {
    this.blockUI.start('Loading data..');
    this.laptopService.getLaptops().subscribe(response => this.laptops = response);
    this.laptopService.getScraperInfo().subscribe(response => {
      this.scraperInfo = response;
      this.blockUI.stop(); });
  }

  searchLaptopBrands() {
    this.laptopService.searchLaptopsByBrand(this.brand).subscribe(response => {
      this.laptops = response;
    });
  }

  reset() {
    this.laptopService.getLaptops().subscribe(response => this.laptops = response);
  }

}
