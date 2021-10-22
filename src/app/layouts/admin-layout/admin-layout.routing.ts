import { Routes } from '@angular/router';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { StatItaCtnComponent } from '../../stat-ita-ctn/stat-ita-ctn.component';
import { StatTunClComponent } from '../../stat-tun-cl/stat-tun-cl.component';
import { StatTunCtnComponent } from '../../stat-tun-ctn/stat-tun-ctn.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'stat-csc',     component: StatCscComponent },
    { path: 'stat-alg',     component: StatAlgComponent },
    { path: 'stat-tun-cl',     component: StatTunClComponent },
    { path: 'stat-tun-ctn',     component: StatTunCtnComponent },
    { path: 'stat-ita-ctn',     component: StatItaCtnComponent },

];
