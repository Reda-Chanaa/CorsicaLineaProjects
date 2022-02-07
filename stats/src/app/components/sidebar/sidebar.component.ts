import { Component, OnInit } from '@angular/core';

declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
    { path: '/stat-csc', title: 'Reporting CSC',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-alg', title: 'Reporting ALG',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-tun', title: 'Reporting TUN',  icon:'design_bullet-list-67', class: '' },
    { path: '/mesure-csc', title: 'Mesure Ventes CSC',  icon:'design_bullet-list-67', class: '' },
    { path: '/mesure-alg', title: 'Mesure Ventes ALG',  icon:'design_bullet-list-67', class: '' },
    { path: '/mesure-tun', title: 'Mesure Ventes TUN',  icon:'design_bullet-list-67', class: '' },
];

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  menuItems: any[];

  constructor() { }

  ngOnInit() {
    this.menuItems = ROUTES.filter(menuItem => menuItem);
  }
  isMobileMenu() {
      if ( window.innerWidth > 991) {
          return false;
      }
      return true;
  };
}
