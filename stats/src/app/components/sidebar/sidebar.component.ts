import { Component, OnInit } from '@angular/core';

declare interface RouteInfo {
  path: string;
  title: string;
  icon: string;
  class: string;
}
export const ROUTES: RouteInfo[] = [
  //{ path: '/dashboard', title: 'Tableau De Bord', icon: 'design_app', class: '' },

  { path: '/stat-csc', title: 'Reporting CSC', icon: 'design_bullet-list-67', class: '' },
  { path: '/stat-alg', title: 'Reporting ALG', icon: 'design_bullet-list-67', class: '' },
  { path: '/stat-tun', title: 'Reporting TUN', icon: 'design_bullet-list-67', class: '' },

  { path: '/mesure-csc', title: 'Mesure Ventes CSC', icon: 'files_paper', class: '' },
  { path: '/mesure-alg', title: 'Mesure Ventes ALG', icon: 'files_paper', class: '' },
  { path: '/mesure-tun', title: 'Mesure Ventes TUN', icon: 'files_paper', class: '' },

  { path: '/chart-csc', title: 'Report Quotidien CSC', icon: 'business_chart-pie-36', class: '' },
  { path: '/chart-alg', title: 'Report Quotidien ALG', icon: 'business_chart-pie-36', class: '' },
  { path: '/chart-tun', title: 'Report Quotidien TUN', icon: 'business_chart-pie-36', class: '' },

  { path: '/profiling', title: 'Profilage', icon: 'business_chart-pie-36', class: '' },

  { path: '/conco-csc', title: 'Concordance CSC', icon: 'loader_refresh', class: '' },
  { path: '/conco-alg', title: 'Concordance ALG', icon: 'loader_refresh', class: '' },
  { path: '/conco-tun', title: 'Concordance TUN', icon: 'loader_refresh', class: '' },

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
    if (window.innerWidth > 991) {
      return false;
    }
    return true;
  };
}
