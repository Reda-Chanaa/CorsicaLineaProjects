import { Routes } from '@angular/router';
import { MesureCscComponent } from '../../mesure-csc/mesure-csc.component';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { StatTunClComponent } from '../../stat-tun/stat-tun.component';
import { MesureAlgComponent } from '../../mesure-alg/mesure-alg.component';
import { MesureTunComponent } from '../../mesure-tun/mesure-tun.component';
import { ChartCscComponent } from '../../chart-csc/chart-csc.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'stat-csc',     component: StatCscComponent },
    { path: 'stat-alg',     component: StatAlgComponent },
    { path: 'stat-tun',     component: StatTunClComponent },
    { path: 'mesure-csc',     component: MesureCscComponent },
    { path: 'mesure-alg',     component: MesureAlgComponent },
    { path: 'mesure-tun',     component: MesureTunComponent },
    { path: 'chart-csc',     component: ChartCscComponent },

];
