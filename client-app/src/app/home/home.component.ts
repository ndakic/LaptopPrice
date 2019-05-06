import { Component, OnInit, OnDestroy } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { BlockUI, NgBlockUI } from 'ng-block-ui';
import { environment } from 'src/environments/environment';
import { Router } from '@angular/router';
import { Laptop } from '../laptop/models/laptop';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  @BlockUI() blockUI: NgBlockUI;

  public laptop: Laptop;

  public laptopBrands: any;
  public processorBrands: any;
  public processorModels: any;
  public processorCores: any;
  public ramGenerations: any;
  public ramAmounts: any;
  public storageTypes: any;
  public storageAmounts: any;
  public screenSizes: any;
  public laptopConditions: any;

  inputForm: FormGroup;

  constructor(
    public laptopService: LaptopService,
    public router: Router
  ) {
    this.laptop = new Laptop();
  }

  ngOnInit() {
    this.inputForm = new FormGroup({
      laptopBrand: new FormControl('', [
        Validators.required
      ]),
      processorBrand: new FormControl('', [
        Validators.required
      ]),
      processorModel: new FormControl('', [
        Validators.required
      ]),
      processorCore: new FormControl('', [
        Validators.required,
      ]),
      ramGeneration: new FormControl('', [
        Validators.required,
      ]),
      ramAmount: new FormControl('', [
        Validators.required,
      ]),
      storageType: new FormControl('', [
        Validators.required,
      ]),
      storageAmount: new FormControl('', [
        Validators.required,
      ]),
      screenSize: new FormControl('', [
        Validators.required,
      ]),
      laptopCondition: new FormControl('', [
        Validators.required,
      ])
    });

    this.loadData();
  }


  get laptopBrand() { return this.inputForm.get('laptopBrand'); }

  get processorBrand() { return this.inputForm.get('processorBrand'); }

  get processorModel() { return this.inputForm.get('processorModel'); }

  get processorCore() { return this.inputForm.get('processorCore'); }

  get ramGeneration() { return this.inputForm.get('ramGeneration'); }

  get ramAmount() { return this.inputForm.get('ramAmount'); }

  get storageType() { return this.inputForm.get('storageType'); }

  get storageAmount() { return this.inputForm.get('storageAmount'); }

  get screenSize() { return this.inputForm.get('screenSize'); }

  get laptopCondition() { return this.inputForm.get('laptopCondition'); }

  laptopData() {
    if (this.inputForm.valid) {
      // this.blockUI.start('Please wait..');
      this.setSpec();
      this.laptopService.setLaptopSpecs(this.laptop);
      // this.delay(3000);
      this.router.navigate(['/result']);
    }
  }

  loadData() {
    this.laptopService.getLaptopBrands().subscribe(brands => this.laptopBrands = brands);
    this.laptopService.getProcessorBrands().subscribe(brands => this.processorBrands = brands);
    this.laptopService.getAllProcessorModels().subscribe(models => this.processorModels = models);
    this.laptopService.getAllProcessorCores().subscribe(cores => this.processorCores = cores);
    this.laptopService.getAllRamGenerations().subscribe(generations => this.ramGenerations = generations);
    this.laptopService.getAllRamAmounts().subscribe(amounts => this.ramAmounts = amounts);
    this.laptopService.getAllStorageTypes().subscribe(types => this.storageTypes = types);
    this.laptopService.getAllStorageAmounts().subscribe(amounts => this.storageAmounts = amounts);
    this.laptopService.getAllScreenSizes().subscribe(sizes => this.screenSizes = sizes);
    this.laptopService.getAllLaptopConditions().subscribe(conditions => this.laptopConditions = conditions);
  }

  setSpec() {
    this.laptop.laptopBrand = this.inputForm.get('laptopBrand').value;
    this.laptop.processorBrand = this.inputForm.get('processorBrand').value;
    this.laptop.processorModel = this.inputForm.get('processorModel').value;
    this.laptop.processorCores = this.inputForm.get('processorCore').value;
    this.laptop.ramGeneration = this.inputForm.get('ramGeneration').value;
    this.laptop.ramAmount = this.inputForm.get('ramAmount').value;
    this.laptop.storageType = this.inputForm.get('storageType').value;
    this.laptop.storageAmount = this.inputForm.get('storageAmount').value;
    this.laptop.screenSize = this.inputForm.get('screenSize').value;
    this.laptop.condition = this.inputForm.get('laptopCondition').value;
  }

  async delay(ms: number) {
    await new Promise(resolve => setTimeout(() => resolve(), ms));
    // this.blockUI.stop();
    // this.router.navigate(['/result']);
  }

}
