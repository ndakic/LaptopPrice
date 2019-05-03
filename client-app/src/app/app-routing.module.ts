import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LaptopComponent } from './laptop/laptop.component';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ResultComponent } from './result/result.component';

const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent,
    canActivate: []
  },
  {
    path: 'laptop',
    component: LaptopComponent,
    canActivate: []
  },
  {
    path: 'about',
    component: AboutComponent,
    canActivate: []
  },
  {
    path: 'result',
    component: ResultComponent,
    canActivate: []
  },
  { path: '**', redirectTo: 'laptop' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
