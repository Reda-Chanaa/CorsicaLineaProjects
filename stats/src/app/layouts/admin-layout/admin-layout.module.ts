import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminLayoutRoutes } from './admin-layout.routing';
import { StatAlgComponent } from '../../stat-alg/stat-alg.component';
import { StatTunClComponent } from '../../stat-tun/stat-tun.component';
import { StatCscComponent } from '../../stat-csc/stat-csc.component';
import { MesureCscComponent } from '../../mesure-csc/mesure-csc.component';
import { ChartsModule } from 'ng2-charts';
import { MatTableExporterModule} from "mat-table-exporter"
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
import { MatSortModule} from '@angular/material/sort'
import { MatIconModule } from '@angular/material/icon';
import { MatDialogModule } from '@angular/material/dialog';
import { MesureAlgComponent } from '../../mesure-alg/mesure-alg.component';
import { MesureTunComponent } from '../../mesure-tun/mesure-tun.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
    ChartsModule,
    NgbModule,
    ToastrModule.forRoot(),
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
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
    MatTableExporterModule
  ],
  declarations: [
    StatAlgComponent,
    StatTunClComponent,
    StatCscComponent,
    MesureCscComponent,
    MesureAlgComponent,
    MesureTunComponent,
  ]
})

export class AdminLayoutModule {}
