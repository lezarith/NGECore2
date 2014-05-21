import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('eow_fbase_stormtrooper')
	mobileTemplate.setLevel(90)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(15)
	mobileTemplate.setAttackSpeed(1.0)
	#mobileTemplate.setWeaponType(1)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setSocialGroup("imperial")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("imperial")
	mobileTemplate.setFactionStatus(1)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_stormtrooper_m.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/carbine/shared_carbine_e11.iff', 1, 1.0)
	weaponTemplates.add(weapontemplate)
	#mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	#mobileTemplate.setDefaultAttack('rangedshot')
	#mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('eow_fbase_stormtrooper', mobileTemplate)
	return