import { Component, OnInit } from '@angular/core';

declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
    { path: '/stat-csc', title: 'Stat CSC',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-alg', title: 'Stat ALG',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-tun-cl', title: 'Stat TUN CL',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-tun-ctn', title: 'Stat TUN CTN',  icon:'design_bullet-list-67', class: '' },
    { path: '/stat-ita-ctn', title: 'Stat ITA CTN',  icon:'design_bullet-list-67', class: '' },
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
