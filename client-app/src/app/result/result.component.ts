// tslint:disable: no-string-literal

import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { Laptop } from '../laptop/models/laptop';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  public laptop: Laptop;
  public laptopPrice: any;

  constructor(
    public laptopService: LaptopService,
    private http: HttpClient,
  ) {
    this.laptop = new Laptop();
   }

  ngOnInit() {
    this.laptopPrice = 0;

    if (this.laptopService.getLaptopSpecs()) {
      this.laptop = this.laptopService.getLaptopSpecs();
      this.getLaptopPrice(this.laptop).subscribe(response => {
        this.laptopPrice = response['result'];
      });
      localStorage.setItem('laptopSpecs', JSON.stringify(this.laptop));
      localStorage.setItem('laptopPrice', this.getLaptopPrice(this.laptop).toString());
    } else {
      if (localStorage.getItem('laptopSpecs') !== null) {
        this.laptop = JSON.parse(localStorage.getItem('laptopSpecs'));
        this.laptopPrice = localStorage.getItem('laptopPrice');
      }
    }
    this.getLaptopPrice(this.laptop).subscribe(response => {
    this.laptopPrice = response['result'];
    });
  }

  getLaptopPrice(laptop) {
    return this.http.post(environment.predictionApi + '/home/predict-price', laptop);
  }
}
