import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LaptopComponent } from './laptop/laptop.component';

const routes: Routes = [
  {
    path: 'laptop',
    component: LaptopComponent,
    canActivate: []
  },
  { path: '**', redirectTo: 'laptop' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
