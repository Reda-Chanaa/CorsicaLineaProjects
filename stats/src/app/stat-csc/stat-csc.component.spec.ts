import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatCscComponent } from './stat-csc.component';

describe('StatCscComponent', () => {
  let component: StatCscComponent;
  let fixture: ComponentFixture<StatCscComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatCscComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatCscComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
