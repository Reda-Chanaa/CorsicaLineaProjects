import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminLayoutRoutes } from './admin-layout.routing';
import { ChartsModule } from 'ng2-charts';
import { MatTableExporterModule } from "mat-table-exporter"
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ToastrModule } from 'ngx-toastr';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatRippleModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatSelectModule } from '@angular/material/select';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatMenuModule } from '@angular/material/menu';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatSortModule } from '@angular/material/sort'
import { MatIconModule } from '@angular/material/icon';
import { MatDialogModule } from '@angular/material/dialog';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatTunClComponent } from '../../stat-tun/stat-tun.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { MesureCscComponent } from '../../mesure-csc/mesure-csc.component';
import { MesureAlgComponent } from '../../mesure-alg/mesure-alg.component';
import { MesureTunComponent } from '../../mesure-tun/mesure-tun.component';
import { DashboardComponent } from '../../dashboard/dashboard.component';
import { ChartCscComponent } from '../../chart-csc/chart-csc.component';
import { ChartAlgComponent } from '../../chart-alg/chart-alg.component';
import { ChartTunComponent } from '../../chart-tun/chart-tun.component';
import { ConcoCscComponent } from '../../conco-csc/conco-csc.component';
import { ConcoAlgComponent } from '../../conco-alg/conco-alg.component';
import { ConcoTunComponent } from '../../conco-tun/conco-tun.component';
import { ProfilingComponent } from '../../profiling/profiling.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
    ChartsModule,
    NgbModule,
    ToastrModule.forRoot(),
    ReactiveFormsModule,
    MatIconModule,
    MatButtonModule,
    MatRippleModule,
    MatDialogModule,
    MatSortModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatMenuModule,
    MatTooltipModule,
    MatTableModule,
    MatPaginatorModule,
    MatExpansionModule,
    MatCheckboxModule,
    MatSlideToggleModule,
    MatTableExporterModule,
    MatDatepickerModule,
    MatNativeDateModule
  ],
  declarations: [
    StatAlgComponent,
    StatTunClComponent,
    StatCscComponent,
    MesureCscComponent,
    MesureAlgComponent,
    MesureTunComponent,
    ChartCscComponent,
    ChartAlgComponent,
    ChartTunComponent,
    DashboardComponent,
    ConcoAlgComponent,
    ConcoCscComponent,
    ConcoTunComponent,
    ProfilingComponent
  ]
})

export class AdminLayoutModule { }
