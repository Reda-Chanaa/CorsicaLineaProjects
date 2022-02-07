import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MesureTunComponent } from './mesure-tun.component';

describe('MesureTunComponent', () => {
  let component: MesureTunComponent;
  let fixture: ComponentFixture<MesureTunComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MesureTunComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MesureTunComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
