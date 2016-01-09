'use strict';

var DailyArtThemesApp = require('./DailyArtThemesApp');
var React = require('react');
var Router = require('react-router');
var Route = Router.Route;

var content = document.getElementById('content');

var Routes = (
	<Route handler={DailyArtThemesApp}>
		<Route name="/" handler={DailyArtThemesApp}/>
	</Route>
);

Router.run(Routes, function (Handler) {
	React.render(<Handler/>, content);
});
