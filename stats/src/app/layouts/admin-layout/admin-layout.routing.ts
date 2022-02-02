import { Routes } from '@angular/router';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { StatTunClComponent } from '../../stat-tun/stat-tun.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'stat-csc',     component: StatCscComponent },
    { path: 'stat-alg',     component: StatAlgComponent },
    { path: 'stat-tun',     component: StatTunClComponent },

];
