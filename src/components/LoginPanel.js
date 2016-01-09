'use strict';

var React = require('react/addons');

// CSS
require('../styles/loginPanel.css');

var LoginPanel = React.createClass({
	render: function() {
		return (
			<div className='login-panel'>
				<form method='post'>
					<input
						type='password'
						name='password'
						placeholder='password'
					/><br/>
					<input
						type='submit'
						value='Log in'
					/>
				</form>
			</div>
		);
	}
});

module.exports = LoginPanel;
