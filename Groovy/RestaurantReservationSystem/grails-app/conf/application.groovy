grails.plugin.springsecurity.userLookup.userDomainClassName = 'pl.dmcs.nsai.User'
grails.plugin.springsecurity.userLookup.authorityJoinClassName = 'pl.dmcs.nsai.UserRole'
grails.plugin.springsecurity.authority.className = 'pl.dmcs.nsai.Role'

grails.plugin.springsecurity.logout.postOnly = false
grails.plugin.springsecurity.securityConfigType = 'InterceptUrlMap'
grails.plugin.springsecurity.interceptUrlMap = [
	[pattern: '/',               access: ['isAuthenticated()']],
	[pattern: '/home/*',         access: ['isAuthenticated()']],
	[pattern: '/error',          access: ['permitAll']],
	[pattern: '/login/*',        access: ['permitAll']],
	[pattern: '/logout/index',   access: ['isAuthenticated()']],
	[pattern: '/index',          access: ['permitAll']],
	[pattern: '/index.gsp',      access: ['permitAll']],
	[pattern: '/register',       access: ['permitAll']],
	[pattern: '/shutdown',       access: ['permitAll']],
	[pattern: '/assets/**',      access: ['permitAll']],
	[pattern: '/**/js/**',       access: ['permitAll']],
	[pattern: '/**/css/**',      access: ['permitAll']],
	[pattern: '/**/images/**',   access: ['permitAll']],
	[pattern: '/**/favicon.ico', access: ['permitAll']]
]

grails.plugin.springsecurity.filterChain.chainMap = [
	[pattern: '/assets/**',      filters: 'none'],
	[pattern: '/**/js/**',       filters: 'none'],
	[pattern: '/**/css/**',      filters: 'none'],
	[pattern: '/**/images/**',   filters: 'none'],
	[pattern: '/**/favicon.ico', filters: 'none'],
	[pattern: '/**',             filters: 'JOINED_FILTERS']
]
