import { Routes } from '@angular/router';
import { MesureCscComponent } from '../../mesure-csc/mesure-csc.component';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { StatTunClComponent } from '../../stat-tun/stat-tun.component';
import { MesureAlgComponent } from '../../mesure-alg/mesure-alg.component';
import { MesureTunComponent } from '../../mesure-tun/mesure-tun.component';
import { ChartCscComponent } from '../../chart-csc/chart-csc.component';
import { ChartAlgComponent } from '../../chart-alg/chart-alg.component';
import { ChartTunComponent } from '../../chart-tun/chart-tun.component';
import { ConcoCscComponent } from '../../conco-csc/conco-csc.component';
import { ConcoAlgComponent } from '../../conco-alg/conco-alg.component';
import { ConcoTunComponent } from '../../conco-tun/conco-tun.component';
import { DashboardComponent } from '../../dashboard/dashboard.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'stat-csc',     component: StatCscComponent },
    { path: 'stat-alg',     component: StatAlgComponent },
    { path: 'stat-tun',     component: StatTunClComponent },
    { path: 'mesure-csc',     component: MesureCscComponent },
    { path: 'mesure-alg',     component: MesureAlgComponent },
    { path: 'mesure-tun',     component: MesureTunComponent },
    { path: 'chart-csc',     component: ChartCscComponent },
    { path: 'chart-alg',     component: ChartAlgComponent },
    { path: 'chart-tun',     component: ChartTunComponent },
    { path: 'conco-csc',     component: ConcoCscComponent },
    { path: 'conco-alg',     component: ConcoAlgComponent },
    { path: 'conco-tun',     component: ConcoTunComponent },
    //{ path: 'dashboard',     component: DashboardComponent },

];
