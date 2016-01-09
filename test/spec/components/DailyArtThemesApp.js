'use strict';

describe('DailyArtThemesApp', () => {
  let React = require('react/addons');
  let DailyArtThemesApp, component;

  beforeEach(() => {
    let container = document.createElement('div');
    container.id = 'content';
    document.body.appendChild(container);

    DailyArtThemesApp = require('components/DailyArtThemesApp.js');
    component = React.createElement(DailyArtThemesApp);
  });

  it('should create a new instance of DailyArtThemesApp', () => {
    expect(component).toBeDefined();
  });
});
