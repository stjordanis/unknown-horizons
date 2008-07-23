# ###################################################
# Copyright (C) 2008 The OpenAnno Team
# team@openanno.org
# This file is part of OpenAnno.
#
# OpenAnno is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

from building import Building
from buildable import BuildableRect
from production import PrimaryProducer
from game.world.nature import Growable
import game.main
import fife

#class GrowingBuilding(BuildableRect, PrimaryProducer):
class GrowingBuilding(BuildableRect, Growable, PrimaryProducer):
	""" Class for stuff that grows, such as trees
	"""
	def __init__(self, x, y, owner, instance = None):
		PrimaryProducer.__init__(self, x, y, owner, instance)
		# assumption: GrowingBuildings can only have one production line
		self.db_actions = game.main.db("SELECT action FROM data.action WHERE building = ? AND action != 'default'", self.id)
		Growable.__init__(self, self)

	@classmethod
	def getInstance(cls, *args, **kwargs):
		kwargs['layer'] = 1
		return super(GrowingBuilding, cls).getInstance(*args, **kwargs)

# the following is the result of an svn conflict
# probably deprecated


#	def update_animation(self):
#		""" Executes next action """
#		try:
#			action = self.cur_action.next()
#			location = fife.Location(game.main.session.view.layers[2])
#			location.setLayerCoordinates(fife.ModelCoordinate(int(self.position[0] + 1), int(self.position[1]), 0))
#			self._instance.act(action, location, True)
#		except StopIteration:
#			# this is a quick & dirty fix, source of the bug has yet to be traced
#			pass
#
#	def restart_animation(self):
#		""" Starts animation from the beginning
#
#		Useful if e.g. a tree is cut down
#		"""
#		self.cur_action = iter(self.actions)
#		self.update_animation()
#		if self.active_production_line == -1:
#			return
#		interval = int(round( self.production[self.active_production_line]['time'] / len(self.actions) ))
#		loops = len(self.actions)-1
#		if loops > 0:
#			game.main.session.scheduler.add_new_object(self.update_animation, self, interval, loops)
#
