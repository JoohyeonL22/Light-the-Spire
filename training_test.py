import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import make_regression
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import MinMaxScaler


#ironclad strike, defend
#ALL_CARDS = ['A Thousand Cuts', 'A Thousand Cuts+1', 'Accuracy', 'Accuracy+1', 'Acrobatics', 'Acrobatics+1', 'Adaptation', 'Adaptation+1', 'Adrenaline', 'Adrenaline+1', 'After Image', 'After Image+1', 'Aggregate', 'Aggregate+1', 'All For One', 'All For One+1', 'All Out Attack', 'All Out Attack+1', 'Alpha', 'Alpha+1', 'Amplify', 'Amplify+1', 'Anger', 'Anger+1', 'Apotheosis', 'Apotheosis+1', 'Armaments', 'Armaments+1', 'AscendersBane', 'Auto Shields', 'Auto Shields+1', 'Backflip', 'Backflip+1', 'Backstab', 'Backstab+1', 'Ball Lightning', 'Ball Lightning+1', 'Bandage Up', 'Bandage Up+1', 'Bane', 'Bane+1', 'Barrage', 'Barrage+1', 'Barricade', 'Barricade+1', 'Bash', 'Bash+1', 'Battle Trance', 'Battle Trance+1', 'BattleHymn', 'BattleHymn+1', 'Beam Cell', 'Beam Cell+1', 'BecomeAlmighty', 'BecomeAlmighty+1', 'Berserk', 'Berserk+1', 'Beta', 'Beta+1', 'Biased Cognition', 'Biased Cognition+1', 'Bite', 'Bite+1', 'Blade Dance', 'Blade Dance+1', 'Blasphemy', 'Blasphemy+1', 'Blind', 'Blind+1', 'Blizzard', 'Blizzard+1', 'Blood for Blood', 'Blood for Blood+1', 'Bloodletting', 'Bloodletting+1', 'Bludgeon', 'Bludgeon+1', 'Blur', 'Blur+1', 'Body Slam', 'Body Slam+1', 'BootSequence', 'BootSequence+1', 'Bouncing Flask', 'Bouncing Flask+1', 'BowlingBash', 'BowlingBash+1', 'Brilliance', 'Brilliance+1', 'Brutality', 'Brutality+1', 'Buffer', 'Buffer+1', 'Bullet Time', 'Bullet Time+1', 'Burn', 'Burn+1', 'Burning Pact', 'Burning Pact+1', 'Burst', 'Burst+1', 'Calculated Gamble', 'Calculated Gamble+1', 'Caltrops', 'Caltrops+1', 'Capacitor', 'Capacitor+1', 'Carnage', 'Carnage+1', 'CarveReality', 'CarveReality+1', 'Catalyst', 'Catalyst+1', 'Chaos', 'Chaos+1', 'Chill', 'Chill+1', 'Choke', 'Choke+1', 'Chrysalis', 'Chrysalis+1', 'Clash', 'Clash+1', 'ClearTheMind', 'ClearTheMind+1', 'Cleave', 'Cleave+1', 'Cloak And Dagger', 'Cloak And Dagger+1', 'Clothesline', 'Clothesline+1', 'Clumsy', 'Cold Snap', 'Cold Snap+1', 'Collect', 'Collect+1', 'Combust', 'Combust+1', 'Compile Driver', 'Compile Driver+1', 'Concentrate', 'Concentrate+1', 'Conclude', 'Conclude+1', 'ConjureBlade', 'ConjureBlade+1', 'Consecrate', 'Consecrate+1', 'Conserve Battery', 'Conserve Battery+1', 'Consume', 'Consume+1', 'Coolheaded', 'Coolheaded+1', 'Core Surge', 'Core Surge+1', 'Corpse Explosion', 'Corpse Explosion+1', 'Corruption', 'Corruption+1', 'Creative AI', 'Creative AI+1', 'Crescendo', 'Crescendo+1', 'Crippling Poison', 'Crippling Poison+1', 'CrushJoints', 'CrushJoints+1', 'CurseOfTheBell', 'CutThroughFate', 'CutThroughFate+1', 'Dagger Spray', 'Dagger Spray+1', 'Dagger Throw', 'Dagger Throw+1', 'Dark Embrace', 'Dark Embrace+1', 'Dark Shackles', 'Dark Shackles+1', 'Darkness', 'Darkness+1', 'Dash', 'Dash+1', 'Dazed', 'Dazed+1', 'Deadly Poison', 'Deadly Poison+1', 'Decay', 'DeceiveReality', 'DeceiveReality+1', 'Deep Breath', 'Deep Breath+1', 'Defend_R', 'Defend_R+1', 'Deflect', 'Deflect+1', 'Defragment', 'Defragment+1', 'Demon Form', 'Demon Form+1', 'DeusExMachina', 'DeusExMachina+1', 'DevaForm', 'DevaForm+1', 'Devotion', 'Devotion+1', 'Die Die Die', 'Die Die Die+1', 'Disarm', 'Disarm+1', 'Discovery', 'Discovery+1', 'Distraction', 'Distraction+1', 'Dodge and Roll', 'Dodge and Roll+1', 'Doom and Gloom', 'Doom and Gloom+1', 'Doppelganger', 'Doppelganger+1', 'Double Energy', 'Double Energy+1', 'Double Tap', 'Double Tap+1', 'Doubt', 'Dramatic Entrance', 'Dramatic Entrance+1', 'Dropkick', 'Dropkick+1', 'Dual Wield', 'Dual Wield+1', 'Dualcast', 'Dualcast+1', 'Echo Form', 'Echo Form+1', 'Electrodynamics', 'Electrodynamics+1', 'EmptyBody', 'EmptyBody+1', 'EmptyFist', 'EmptyFist+1', 'EmptyMind', 'EmptyMind+1', 'Endless Agony', 'Endless Agony+1', 'Enlightenment', 'Enlightenment+1', 'Entrench', 'Entrench+1', 'Envenom', 'Envenom+1', 'Eruption', 'Eruption+1', 'Escape Plan', 'Escape Plan+1', 'Establishment', 'Establishment+1', 'Evaluate', 'Evaluate+1', 'Eviscerate', 'Eviscerate+1', 'Evolve', 'Evolve+1', 'Exhume', 'Exhume+1', 'Expertise', 'Expertise+1', 'Expunger', 'Expunger+1', 'FTL', 'FTL+1', 'FameAndFortune', 'FameAndFortune+1', 'Fasting2', 'Fasting2+1', 'FearNoEvil', 'FearNoEvil+1', 'Feed', 'Feed+1', 'Feel No Pain', 'Feel No Pain+1', 'Fiend Fire', 'Fiend Fire+1', 'Finesse', 'Finesse+1', 'Finisher', 'Finisher+1', 'Fire Breathing', 'Fire Breathing+1', 'Fission', 'Fission+1', 'Flame Barrier', 'Flame Barrier+1', 'Flash of Steel', 'Flash of Steel+1', 'Flechettes', 'Flechettes+1', 'Flex', 'Flex+1', 'FlurryOfBlows', 'FlurryOfBlows+1', 'Flying Knee', 'Flying Knee+1', 'FlyingSleeves', 'FlyingSleeves+1', 'FollowUp', 'FollowUp+1', 'Footwork', 'Footwork+1', 'Force Field', 'Force Field+1', 'ForeignInfluence', 'ForeignInfluence+1', 'Forethought', 'Forethought+1', 'Fusion', 'Fusion+1', 'Gash', 'Gash+1', 'Genetic Algorithm', 'Genetic Algorithm+1', 'Ghostly', 'Ghostly Armor', 'Ghostly Armor+1', 'Ghostly+1', 'Glacier', 'Glacier+1', 'Glass Knife', 'Glass Knife+1', 'Go for the Eyes', 'Go for the Eyes+1', 'Good Instincts', 'Good Instincts+1', 'Grand Finale', 'Grand Finale+1', 'Halt', 'Halt+1', 'HandOfGreed', 'HandOfGreed+1', 'Havoc', 'Havoc+1', 'Headbutt', 'Headbutt+1', 'Heatsinks', 'Heatsinks+1', 'Heavy Blade', 'Heavy Blade+1', 'Heel Hook', 'Heel Hook+1', 'Hello World', 'Hello World+1', 'Hemokinesis', 'Hemokinesis+1', 'Hologram', 'Hologram+1', 'Hyperbeam', 'Hyperbeam+1', 'Immolate', 'Immolate+1', 'Impatience', 'Impatience+1', 'Impervious', 'Impervious+1', 'Indignation', 'Indignation+1', 'Infernal Blade', 'Infernal Blade+1', 'Infinite Blades', 'Infinite Blades+1', 'Inflame', 'Inflame+1', 'Injury', 'InnerPeace', 'InnerPeace+1', 'Insight', 'Insight+1', 'Intimidate', 'Intimidate+1', 'Iron Wave', 'Iron Wave+1', 'J.A.X.', 'J.A.X.+1', 'Jack Of All Trades', 'Jack Of All Trades+1', 'Judgement', 'Judgement+1', 'Juggernaut', 'Juggernaut+1', 'JustLucky', 'JustLucky+1', 'Leap', 'Leap+1', 'Leg Sweep', 'Leg Sweep+1', 'LessonLearned', 'LessonLearned+1', 'LikeWater', 'LikeWater+1', 'Limit Break', 'Limit Break+1', 'LiveForever', 'LiveForever+1', 'Lockon', 'Lockon+1', 'Loop', 'Loop+1', 'Machine Learning', 'Machine Learning+1', 'Madness', 'Madness+1', 'Magnetism', 'Magnetism+1', 'Malaise', 'Malaise+1', 'Master of Strategy', 'Master of Strategy+1', 'MasterReality', 'MasterReality+1', 'Masterful Stab', 'Masterful Stab+1', 'Mayhem', 'Mayhem+1', 'Meditate', 'Meditate+1', 'Melter', 'Melter+1', 'MentalFortress', 'MentalFortress+1', 'Metallicize', 'Metallicize+1', 'Metamorphosis', 'Metamorphosis+1', 'Meteor Strike', 'Meteor Strike+1', 'Mind Blast', 'Mind Blast+1', 'Miracle', 'Miracle+1', 'Multi-Cast', 'Multi-Cast+1', 'Necronomicurse', 'Neutralize', 'Neutralize+1', 'Night Terror', 'Night Terror+1', 'Nirvana', 'Nirvana+1', 'Normality', 'Noxious Fumes', 'Noxious Fumes+1', 'Offering', 'Offering+1', 'Omega', 'Omega+1', 'Omniscience', 'Omniscience+1', 'Outmaneuver', 'Outmaneuver+1', 'Pain', 'Panacea', 'Panacea+1', 'Panache', 'Panache+1', 'PanicButton', 'PanicButton+1', 'Parasite', 'PathToVictory', 'PathToVictory+1', 'Perfected Strike', 'Perfected Strike+1', 'Perseverance', 'Perseverance+1', 'Phantasmal Killer', 'Phantasmal Killer+1', 'PiercingWail', 'PiercingWail+1', 'Poisoned Stab', 'Poisoned Stab+1', 'Pommel Strike', 'Pommel Strike+1', 'Power Through', 'Power Through+1', 'Pray', 'Pray+1', 'Predator', 'Predator+1', 'Prepared', 'Prepared+1', 'Pride', 'Prostrate', 'Prostrate+1', 'Protect', 'Protect+1', 'Pummel', 'Pummel+1', 'Purity', 'Purity+1', 'Quick Slash', 'Quick Slash+1', 'Rage', 'Rage+1', 'Ragnarok', 'Ragnarok+1', 'Rainbow', 'Rainbow+1', 'Rampage', 'Rampage+1', 'ReachHeaven', 'ReachHeaven+1', 'Reaper', 'Reaper+1', 'Reboot', 'Reboot+1', 'Rebound', 'Rebound+1', 'Reckless Charge', 'Reckless Charge+1', 'Recycle', 'Recycle+1', 'Redo', 'Redo+1', 'Reflex', 'Reflex+1', 'Regret', 'Reinforced Body', 'Reinforced Body+1', 'Reprogram', 'Reprogram+1', 'Riddle With Holes', 'Riddle With Holes+1', 'Rip and Tear', 'Rip and Tear+1', 'RitualDagger', 'RitualDagger+1', 'Rupture', 'Rupture+1', 'Sadistic Nature', 'Sadistic Nature+1', 'Safety', 'Safety+1', 'Sanctity', 'Sanctity+1', 'SandsOfTime', 'SandsOfTime+1', 'SashWhip', 'SashWhip+1', 'Scrape', 'Scrape+1', 'Scrawl', 'Scrawl+1', 'Searing Blow', 'Searing Blow+1', 'Second Wind', 'Second Wind+1', 'Secret Technique', 'Secret Technique+1', 'Secret Weapon', 'Secret Weapon+1', 'Seeing Red', 'Seeing Red+1', 'Seek', 'Seek+1', 'Self Repair', 'Self Repair+1', 'Sentinel', 'Sentinel+1', 'Setup', 'Setup+1', 'Sever Soul', 'Sever Soul+1', 'Shame', 'Shiv', 'Shiv+1', 'Shockwave', 'Shockwave+1', 'Shrug It Off', 'Shrug It Off+1', 'SignatureMove', 'SignatureMove+1', 'Skewer', 'Skewer+1', 'Skim', 'Skim+1', 'Slice', 'Slice+1', 'Slimed', 'Slimed+1', 'Smite', 'Smite+1', 'SpiritShield', 'SpiritShield+1', 'Spot Weakness', 'Spot Weakness+1', 'Stack', 'Stack+1', 'Static Discharge', 'Static Discharge+1', 'Steam', 'Steam Power', 'Steam Power+1', 'Steam+1', 'Storm', 'Storm of Steel', 'Storm of Steel+1', 'Storm+1', 'Streamline', 'Streamline+1', 'Strike_R', 'Strike_R+1', 'Study', 'Study+1', 'Sucker Punch', 'Sucker Punch+1', 'Sunder', 'Sunder+1', 'Survivor', 'Survivor+1', 'Sweeping Beam', 'Sweeping Beam+1', 'Swift Strike', 'Swift Strike+1', 'Swivel', 'Swivel+1', 'Sword Boomerang', 'Sword Boomerang+1', 'Tactician', 'Tactician+1', 'TalkToTheHand', 'TalkToTheHand+1', 'Tantrum', 'Tantrum+1', 'Tempest', 'Tempest+1', 'Terror', 'Terror+1', 'The Bomb', 'The Bomb+1', 'Thinking Ahead', 'Thinking Ahead+1', 'ThirdEye', 'ThirdEye+1', 'ThroughViolence', 'ThroughViolence+1', 'Thunder Strike', 'Thunder Strike+1', 'Thunderclap', 'Thunderclap+1', 'Tools of the Trade', 'Tools of the Trade+1', 'Transmutation', 'Transmutation+1', 'Trip', 'Trip+1', 'True Grit', 'True Grit+1', 'Turbo', 'Turbo+1', 'Twin Strike', 'Twin Strike+1', 'Underhanded Strike', 'Underhanded Strike+1', 'Undo', 'Undo+1', 'Unload', 'Unload+1', 'Uppercut', 'Uppercut+1', 'Vault', 'Vault+1', 'Vengeance', 'Vengeance+1', 'Venomology', 'Venomology+1', 'Vigilance', 'Vigilance+1', 'Violence', 'Violence+1', 'Void', 'Void+1', 'Wallop', 'Wallop+1', 'Warcry', 'Warcry+1', 'WaveOfTheHand', 'WaveOfTheHand+1', 'Weave', 'Weave+1', 'Well Laid Plans', 'Well Laid Plans+1', 'WheelKick', 'WheelKick+1', 'Whirlwind', 'Whirlwind+1', 'White Noise', 'White Noise+1', 'Wild Strike', 'Wild Strike+1', 'WindmillStrike', 'WindmillStrike+1', 'Wireheading', 'Wireheading+1', 'Wish', 'Wish+1', 'Worship', 'Worship+1', 'Wound', 'Wound+1', 'Wraith Form v2', 'Wraith Form v2+1', 'WreathOfFlame', 'WreathOfFlame+1', 'Writhe', 'Zap', 'Zap+1']
ALL_IRONCLAD = ['Anger', 'Anger+1', 'Armaments', 'Armaments+1', 'Barricade', 'Barricade+1', 'Bash', 'Bash+1', 'Battle Trance', 'Battle Trance+1', 'Berserk', 'Berserk+1', 'Blood for Blood', 'Blood for Blood+1', 'Bloodletting', 'Bloodletting+1', 'Bludgeon', 'Bludgeon+1', 'Body Slam', 'Body Slam+1', 'Brutality', 'Brutality+1', 'Burning Pact', 'Burning Pact+1', 'Carnage', 'Carnage+1', 'Clash', 'Clash+1', 'Cleave', 'Cleave+1', 'Clothesline', 'Clothesline+1', 'Combust', 'Combust+1', 'Corruption', 'Corruption+1', 'Dark Embrace', 'Dark Embrace+1', 'Defend_R', 'Defend_R+1', 'Demon Form', 'Demon Form+1', 'Disarm', 'Disarm+1', 'Double Tap', 'Double Tap+1', 'Dropkick', 'Dropkick+1', 'Dual Wield', 'Dual Wield+1', 'Entrench', 'Entrench+1', 'Evolve', 'Evolve+1', 'Exhume', 'Exhume+1', 'Feed', 'Feed+1', 'Feel No Pain', 'Feel No Pain+1', 'Fiend Fire', 'Fiend Fire+1', 'Fire Breathing', 'Fire Breathing+1', 'Flame Barrier', 'Flame Barrier+1', 'Flex', 'Flex+1', 'Ghostly Armor', 'Ghostly Armor+1', 'Havoc', 'Havoc+1', 'Headbutt', 'Headbutt+1', 'Heavy Blade', 'Heavy Blade+1', 'Hemokinesis', 'Hemokinesis+1', 'Immolate', 'Immolate+1', 'Impervious', 'Impervious+1', 'Infernal Blade', 'Infernal Blade+1', 'Inflame', 'Inflame+1', 'Intimidate', 'Intimidate+1', 'Iron Wave', 'Iron Wave+1', 'Juggernaut', 'Juggernaut+1', 'Limit Break', 'Limit Break+1', 'Metallicize', 'Metallicize+1', 'Offering', 'Offering+1', 'Perfected Strike', 'Perfected Strike+1', 'Pommel Strike', 'Pommel Strike+1', 'Power Through', 'Power Through+1', 'Pummel', 'Pummel+1', 'Rage', 'Rage+1', 'Rampage', 'Rampage+1', 'Reaper', 'Reaper+1', 'Reckless Charge', 'Reckless Charge+1', 'Rupture', 'Rupture+1', 'Searing Blow', 'Searing Blow+1', 'Second Wind', 'Second Wind+1', 'Seeing Red', 'Seeing Red+1', 'Sentinel', 'Sentinel+1', 'Sever Soul', 'Sever Soul+1', 'Shockwave', 'Shockwave+1', 'Shrug It Off', 'Shrug It Off+1', 'Spot Weakness', 'Spot Weakness+1', 'Strike_R', 'Strike_R+1', 'Sword Boomerang', 'Sword Boomerang+1', 'Thunderclap', 'Thunderclap+1', 'True Grit', 'True Grit+1', 'Twin Strike', 'Twin Strike+1', 'Uppercut', 'Uppercut+1', 'Warcry', 'Warcry+1', 'Whirlwind', 'Whirlwind+1', 'Wild Strike', 'Wild Strike+1', 'Apotheosis', 'Apotheosis+1', 'AscendersBane', 'Bandage Up', 'Bandage Up+1', 'Bite', 'Bite+1', 'Blind', 'Blind+1', 'Chrysalis', 'Chrysalis+1', 'Dark Shackles', 'Dark Shackles+1', 'Dramatic Entrance', 'Dramatic Entrance+1', 'Deep Breath', 'Deep Breath+1', 'Discovery', 'Discovery+1', 'Enlightenment', 'Enlightenment+1', 'Flash of Steel', 'Flash of Steel+1', 'Finesse', 'Finesse+1', 'Forethought', 'Forethought+1', 'Good Instincts', 'Good Instincts+1', 'HandOfGreed', 'HandOfGreed+1', 'Impatience', 'Impatience+1', 'Jack Of All Trades', 'Jack Of All Trades+1', 'J.A.X.', 'J.A.X.+1', 'Madness', 'Madness+1', 'Magnetism', 'Magnetism+1', 'Master of Strategy', 'Master of Strategy+1', 'Mayhem', 'Mayhem+1', 'Metamorphosis', 'Metamorphosis+1', 'Mind Blast', 'Mind Blast+1', 'Panacea', 'Panacea+1', 'Panache', 'Panache+1', 'PanicButton', 'PanicButton+1', 'Purity', 'Purity+1', 'RitualDagger', 'RitualDagger+1', 'Sadistic Nature', 'Sadistic Nature+1', 'Secret Technique', 'Secret Technique+1', 'Secret Weapon', 'Secret Weapon+1', 'Swift Strike', 'Swift Strike+1', 'The Bomb', 'The Bomb+1', 'Thinking Ahead', 'Thinking Ahead+1', 'ThroughViolence', 'ThroughViolence+1', 'Transmutation', 'Transmutation+1', 'Trip', 'Trip+1', 'Violence', 'Violence+1', 'Clumsy', 'CurseOfTheBell', 'Decay', 'Doubt', 'Injury', 'Normality', 'Necronomicurse', 'Pain', 'Parasite', 'Pride', 'Regret', 'Shame', 'Writhe']
ALL_IRONCLAD.append("damage_taken")

dataset = pd.read_csv("D:/Documents/Jaw Worm_0.csv", names=ALL_IRONCLAD)

train_dataset2 = dataset.sample(frac=0.8,random_state=0)
test_dataset2 = dataset.drop(train_dataset2.index)
train_labels2 = train_dataset2.pop('damage_taken')
test_labels2 = test_dataset2.pop('damage_taken')

#train_dataset = np.transpose(train_dataset2).to_numpy()
#test_dataset = np.transpose(test_dataset2).to_numpy()
train_dataset = train_dataset2.to_numpy()
test_dataset = test_dataset2.to_numpy()
train_labels = train_labels2.to_numpy()
test_labels = test_labels2.to_numpy()
#print(train_dataset.shape)


EPOCHS = 500

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(400, input_shape=(len(train_dataset[0]),), activation='relu'),
  tf.keras.layers.Dropout(.2),
  tf.keras.layers.Dense(200, activation='relu'),
  tf.keras.layers.Dropout(.1),
  tf.keras.layers.Dense(1)
])

model.summary()
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=.001),
    loss='mean_absolute_error',
    metrics=['mean_absolute_error', 'mean_squared_error'])

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')




hist = model.fit(train_dataset, train_labels, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[PrintDot()])

#print(hist.history['loss'])
#print(hist.history['val_loss'])

#print(hist.history['acc'])
#print(hist.history['val_acc'])


fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

#acc_ax.plot(hist.history['acc'], 'b', label='train acc')
#acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()


print("dropout 400, 200")

test_scores = model.evaluate(test_dataset, test_labels, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])
model.save("D:/Documents/my_model.h5")



#model.save("D:/Documents/my_model.h5")
#model.save("my_model")
#model = keras.models.load_model("D:/Documents/resnet_model.h5")
model = keras.models.load_model("D:/Documents/my_model.h5")

test_scores = model.evaluate(test_dataset, test_labels, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])

#predcit with temp_list input
temp_list = np.zeros((1,242))
temp_list[0][6] = 1
temp_list[0][38] = 4
temp_list[0][120] = 1
temp_list[0][124] = 2
temp_list[0][132] = 4

temp2_labels = []
temp2_labels.append(3)
temp_labels = np.array(temp2_labels)
#print("Test loss:", test_scores[0])
#rint("Test accuracy:", test_scores[1])
y_predict1 = model.predict(temp_list)
print("predcit_loss_yes card :", y_predict1)
temp_list[0][6] = 0 #강타 없을 때 예측 체력 손실 값
y_predict2 = model.predict(temp_list)
print("predcit_loss_no card :", y_predict2)
print("if you use this card, hp_gain : ", y_predict2-y_predict1)




"""
learning_rate = 0.01
training_steps =10000
xy = np.loadtxt("D:/Documents/Jaw Worm.csv", delimiter=',', dtype=np.float32) 

X_DATA = xy[:, 0:-1]
Y_DATA = xy[:, [-1]]

W = tf.Variable(tf.random.normal([242,1], 0, 1), name='weight')
b = tf.Variable(tf.random.normal([1], 0, 1), name='bias')

def predict(x):
    return tf.matmul(x,W)+b

for i in range(training_steps):
    with tf.GradientTape() as tape:
        cost_val = tf.reduce_mean((tf.square(predict(X_DATA)-Y_DATA)))
    W_gradient, b_gradient = tape.gradient(cost_val, [W, b])
    W.assign_sub(learning_rate*W_gradient)
    b.assign_sub(learning_rate*b_gradient)
    
    if i % 1000 == 0 :
        print("steps{:5} : {:5.3f}".format(i, cost_val.numpy()))
"""

"""
dataset = pd.read_csv("D:/Documents/Jaw Worm.csv", names=ALL_IRONCLAD)
train_dataset2 = dataset.sample(frac=0.8,random_state=0)
test_dataset2 = dataset.drop(train_dataset2.index)
train_labels2 = train_dataset2.pop('damage_taken')
test_labels2 = test_dataset2.pop('damage_taken')

train_dataset3 = train_dataset2.to_numpy()
train_dataset = train_dataset3.astype('float64')
train_labels3 = train_labels2.to_numpy().reshape(-1,1)
train_labels = train_labels3.astype('float64')

test_dataset3 = test_dataset2.to_numpy()
test_dataset = test_dataset3.astype('float64')
test_labels3 = test_labels2.to_numpy().reshape(-1,1)
test_labels = test_labels3.astype('float64')
X, y = make_regression(n_samples=100, n_features=3, bias=10.0, noise=10.0, random_state=1)

# 뒤에 tensorflow 및 keras는 제거 필요
X = np.insert(X, 0, 1, axis=1)
y = np.expand_dims(y, axis=1)

train_x = X[:80]
test_x = X[80:]

train_y = y[:80]
test_y = y[80:]
train_dataset = train_x
train_labels = train_y

print(train_labels)


class mlraWithTF():
    def __init__(self):
        self.epochs = 100
        self.learning_rate = 0.01
        #Variable setting
        self.w = tf.Variable(tf.random.uniform([4,1], dtype=tf.dtypes.float64 ))
        self.b = tf.Variable(tf.zeros([1], dtype=tf.dtypes.float64 ))

    def buildModel(self, x, y):
        with tf.GradientTape() as tape:
            
            hypothesis = tf.matmul(x, self.w) + self.b
            loss = tf.reduce_mean(tf.square(hypothesis - y))
            loss_w, loss_b = tape.gradient(loss, [self.w, self.b])
        self.w.assign_sub(loss_w * self.learning_rate)
        self.b.assign_sub(loss_b * self.learning_rate)
        return loss
    
    def trainModel(self, x, y):
       data = tf.data.Dataset.from_tensor_slices((x, y))
       data = data.shuffle(buffer_size=50).batch(10)

       loss_mem = []
       for e in range(self.epochs):
           for each, (x,y) in enumerate(data):
               loss = self.buildModel(x, y)
           print('epoch {0}: loss is {1:.4f}'.format(e, float(loss)))
           #print(self.w) # each card weights
           loss_mem.append(loss)
       return loss_mem
   
    def evalModel(self, x, y):
        y_hat = tf.matmul(x, self.w) + self.b
        mse = tf.reduce_mean(tf.square(y_hat - y))
        rmse = tf.sqrt(mse)
        return rmse
   
model = mlraWithTF()
loss_mem = model.trainModel(train_dataset, train_labels)

x_epoch = list(range(len(loss_mem)))

plt.plot(x_epoch, loss_mem)
plt.xlabel('epochs')
plt.ylabel('Loss status')
plt.show()
"""


"""
ALL_IRONCLAD1 = ['Anger', 'Anger+1', 'Armaments', 'Armaments+1', 'Barricade', 'Barricade+1', 'Bash', 'Bash+1', 'Battle Trance', 'Battle Trance+1', 'Berserk', 'Berserk+1', 'Blood for Blood', 'Blood for Blood+1', 'Bloodletting', 'Bloodletting+1', 'Bludgeon', 'Bludgeon+1', 'Body Slam', 'Body Slam+1', 'Brutality', 'Brutality+1', 'Burning Pact', 'Burning Pact+1', 'Carnage', 'Carnage+1', 'Clash', 'Clash+1', 'Cleave', 'Cleave+1', 'Clothesline', 'Clothesline+1', 'Combust', 'Combust+1', 'Corruption', 'Corruption+1', 'Dark Embrace', 'Dark Embrace+1', 'Defend_R', 'Defend_R+1', 'Demon Form', 'Demon Form+1', 'Disarm', 'Disarm+1', 'Double Tap', 'Double Tap+1', 'Dropkick', 'Dropkick+1', 'Dual Wield', 'Dual Wield+1', 'Entrench', 'Entrench+1', 'Evolve', 'Evolve+1', 'Exhume', 'Exhume+1', 'Feed', 'Feed+1', 'Feel No Pain', 'Feel No Pain+1', 'Fiend Fire', 'Fiend Fire+1', 'Fire Breathing', 'Fire Breathing+1', 'Flame Barrier', 'Flame Barrier+1', 'Flex', 'Flex+1', 'Ghostly Armor', 'Ghostly Armor+1', 'Havoc', 'Havoc+1', 'Headbutt', 'Headbutt+1', 'Heavy Blade', 'Heavy Blade+1', 'Hemokinesis', 'Hemokinesis+1', 'Immolate', 'Immolate+1', 'Impervious', 'Impervious+1', 'Infernal Blade', 'Infernal Blade+1', 'Inflame', 'Inflame+1', 'Intimidate', 'Intimidate+1', 'Iron Wave', 'Iron Wave+1', 'Juggernaut', 'Juggernaut+1', 'Limit Break', 'Limit Break+1', 'Metallicize', 'Metallicize+1', 'Offering', 'Offering+1', 'Perfected Strike', 'Perfected Strike+1', 'Pommel Strike', 'Pommel Strike+1', 'Power Through', 'Power Through+1', 'Pummel', 'Pummel+1', 'Rage', 'Rage+1', 'Rampage', 'Rampage+1', 'Reaper', 'Reaper+1', 'Reckless Charge', 'Reckless Charge+1', 'Rupture', 'Rupture+1', 'Searing Blow', 'Searing Blow+1', 'Second Wind', 'Second Wind+1', 'Seeing Red', 'Seeing Red+1', 'Sentinel', 'Sentinel+1', 'Sever Soul', 'Sever Soul+1', 'Shockwave', 'Shockwave+1', 'Shrug It Off', 'Shrug It Off+1', 'Spot Weakness', 'Spot Weakness+1', 'Strike_R', 'Strike_R+1', 'Sword Boomerang', 'Sword Boomerang+1', 'Thunderclap', 'Thunderclap+1', 'True Grit', 'True Grit+1', 'Twin Strike', 'Twin Strike+1', 'Uppercut', 'Uppercut+1', 'Warcry', 'Warcry+1', 'Whirlwind', 'Whirlwind+1', 'Wild Strike', 'Wild Strike+1', 'Apotheosis', 'Apotheosis+1', 'AscendersBane', 'Bandage Up', 'Bandage Up+1', 'Bite', 'Bite+1', 'Blind', 'Blind+1', 'Chrysalis', 'Chrysalis+1', 'Dark Shackles', 'Dark Shackles+1', 'Dramatic Entrance', 'Dramatic Entrance+1', 'Deep Breath', 'Deep Breath+1', 'Discovery', 'Discovery+1', 'Enlightenment', 'Enlightenment+1', 'Flash of Steel', 'Flash of Steel+1', 'Finesse', 'Finesse+1', 'Forethought', 'Forethought+1', 'Good Instincts', 'Good Instincts+1', 'HandOfGreed', 'HandOfGreed+1', 'Impatience', 'Impatience+1', 'Jack Of All Trades', 'Jack Of All Trades+1', 'J.A.X.', 'J.A.X.+1', 'Madness', 'Madness+1', 'Magnetism', 'Magnetism+1', 'Master of Strategy', 'Master of Strategy+1', 'Mayhem', 'Mayhem+1', 'Metamorphosis', 'Metamorphosis+1', 'Mind Blast', 'Mind Blast+1', 'Panacea', 'Panacea+1', 'Panache', 'Panache+1', 'PanicButton', 'PanicButton+1', 'Purity', 'Purity+1', 'RitualDagger', 'RitualDagger+1', 'Sadistic Nature', 'Sadistic Nature+1', 'Secret Technique', 'Secret Technique+1', 'Secret Weapon', 'Secret Weapon+1', 'Swift Strike', 'Swift Strike+1', 'The Bomb', 'The Bomb+1', 'Thinking Ahead', 'Thinking Ahead+1', 'ThroughViolence', 'ThroughViolence+1', 'Transmutation', 'Transmutation+1', 'Trip', 'Trip+1', 'Violence', 'Violence+1', 'Clumsy', 'CurseOfTheBell', 'Decay', 'Doubt', 'Injury', 'Normality', 'Necronomicurse', 'Pain', 'Parasite', 'Pride', 'Regret', 'Shame', 'Writhe']
ALL_IRONCLAD2 = []

for i in ALL_IRONCLAD1:
    temp = i.replace("+", "-")
    ALL_IRONCLAD2.append(temp)

ALL_IRONCLAD = []

for i in ALL_IRONCLAD2:
    temp2 = i.replace(" ", "_")
    ALL_IRONCLAD.append(temp2)

ALL_IRONCLAD.append("damage_taken")
dataset = pd.read_csv("D:Documents//Jaw Worm.csv", names=ALL_IRONCLAD)

y_val= dataset['damage_taken']
x_data=dataset.drop('damage_taken', axis=1)

X_train, X_eval,y_train,y_eval=train_test_split(x_data,y_val,test_size=0.2,random_state=101)

scaler_model = MinMaxScaler()
scaler_model.fit(X_train)

X_train=pd.DataFrame(scaler_model.transform(X_train),columns=X_train.columns,index=X_train.index)

scaler_model.fit(X_eval)

X_eval=pd.DataFrame(scaler_model.transform(X_eval),columns=X_eval.columns,index=X_eval.index)

#Creating Feature Columns
feat_cols=[]
for cols in dataset.columns[:-1]:
    column=tf.feature_column.numeric_column(cols)
    feat_cols.append(column)
    
#print(feat_cols)

#The estimator model
model=tf.estimator.DNNRegressor(hidden_units=[6,10,6],feature_columns=feat_cols)

#the input function
input_func=tf.compat.v1.estimator.inputs.pandas_input_fn(X_train,y_train,batch_size=10,num_epochs=1000,shuffle=True)

#Training the model
model.train(input_fn=input_func,steps=1000)
"""


"""
train_dataset2 = dataset.sample(frac=0.8,random_state=0)
test_dataset2 = dataset.drop(train_dataset2.index)
train_labels2 = train_dataset2.pop('damage_taken')
test_labels2 = test_dataset2.pop('damage_taken')


train_dataset = np.transpose(train_dataset2).to_numpy()
test_dataset = np.transpose(test_dataset2).to_numpy()
train_labels = train_labels2.to_numpy()
test_labels = test_labels2.to_numpy()

class Model(object):
    def __init__(self, x, y):
        self.W = tf.Variable(tf.random.normal((len(x), len(x[0]))))
        self.b = tf.Variable(tf.random.normal((len(y),)))

    def __call__(self, x):
        return self.W * x + self.b

def loss(predicted_y, desired_y):
    return tf.reduce_sum(tf.square(predicted_y - desired_y))

optimizer = tf.optimizers.SGD(0.1)

def train(model, inputs, outputs):
    with tf.GradientTape() as t:
        current_loss = loss(model(inputs), outputs)
    grads = t.gradient(current_loss, [model.W, model.b])
    optimizer.apply_gradients(zip(grads,[model.W, model.b]))

model = Model(train_dataset, train_labels)


for i in range(100):
    train(model,train_dataset,train_labels)
"""

#sns.pairplot(train_dataset[["Strike_R", "Defend_R"]], diag_kind="kde")
#print(train_dataset) #1026 x 242 dim
#print(train_labels) #1 x 1026 dim
#print(train_dataset.isna().sum())

"""
def build_model():
    model = keras.Sequential([
    layers.Dense(400, input_shape=[len(train_dataset.keys())], activation='relu'),
    layers.Dropout(.2),
    layers.Dense(40, activation='relu'),
    layers.Dropout(.1),
    layers.Dense(1)
    ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mae',optimizer=optimizer, metrics=['mae', 'mse'])
    return model

model = build_model()
model.summary()
"""


"""
#sample
example_batch = train_dataset[:10]
example_result = model.predict(example_batch)
print(example_result)
"""

"""
#epoch가 끝날 때마다 출력
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')


EPOCHS = 1000
history = model.fit(train_dataset, train_labels, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure(figsize=(8,12))

  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [damage_taken]')
  plt.plot(hist['epoch'], hist['mae'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$damage_taken^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()

plot_history(history)
"""



