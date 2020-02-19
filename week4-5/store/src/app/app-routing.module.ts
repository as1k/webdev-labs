import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ProductItemComponent} from './product-item/product-item.component';
import {ProductListComponent} from './product-list/product-list.component';
import {CategoryComponent} from "./category/category.component";

const routes: Routes = [
  // { path: '', component: ProductListComponent},
  // { path: 'product-item/:id', component: ProductItemComponent},
  { path: 'products', component: ProductListComponent},
  { path: '', redirectTo: '/products', pathMatch: 'full'},
  { path: 'category/:id/product-id/:id', component: ProductItemComponent},
  { path: 'category/:id', component: CategoryComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
