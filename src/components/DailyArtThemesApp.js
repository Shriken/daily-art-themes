'use strict';

var React = require('react/addons');

var LoginPanel = require('./LoginPanel');

// CSS
require('../styles/main.css');

var DailyArtThemesApp = React.createClass({
	render: function() {
		return (
			<div className='main'>
				<LoginPanel/>
			</div>
		);
	}
});

module.exports = DailyArtThemesApp;
