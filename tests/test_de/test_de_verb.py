import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

verb_tempus_perfekt_sentences = [
  "- Hast du etwas von Helmut gehört? - Ja, gestern bin ich ihm zufällig begegnet.",
  "Vor einem Jahr ist ein Beamter in den Ruhestand getreten.",
  "Er ist zu spät gekommen. Er hat den Bus verpasst.",
  "Das da ist Eva? Kaum zu glauben, wie groß sie im letzten Jahr gewachsen ist.",
  "Sind Sie durch ganz Europa gereist?",
  "Die Bundesrepublik hat gegen Frankreich mit 2:1 gewonnen.",
  "Diese Anzeige hat gestern in der Zeitung gestanden.",
  "Wir haben uns erst vor einem Monat in München kennen gelernt.",
  "Letzte Nacht habe ich nicht gut geschlafen, ich bin fast nicht eingeschlafen.",
  "Endlich hat man diesen Vertrag abgeschlossen.",
  "Diese Nachricht hat uns tief ergriffen.",
  "Heute hat der Chef mit den Gästen aus Japan ein Gespräch geführt.",
  "Letztes Jahr sind die Preise um drei Prozent gestiegen.",
  "Was hast du denn im letzten Test für eine Note bekommen?",
  "- Was ist richtig? - Was ist hier denn passiert?",
  "Haben Sie sich mit dem Sekretariat in Verbindung gesetzt?",
  "Wer hat eigentlich bestimmt, dass das Institut geschlossen wird?",
  "Sie hat mir ihren Freund vorgestellt.",
  "Die Zeitung hat die Worte des Bundespräsidenten veröffentlicht.",
  "Mein Chef hat sein Versprechen gebrochen.",
]

def test_verb_tempus_perfekt():
  sentences = verb_tempus_perfekt_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_tempus_perfekt"]})
  display(sentences, nlp)

verb_tempus_prätertum_sentences = [
  "Vor kurzem lud er mich zum Abendessen im Restaurant ein.",
  "Gestern nahm er eine E-Mail in der Hand.",
  "An der Wand hing vorher ein schönes Bild von München.",
  "Gestern traf ich zufällig meinen alten Freund im Stadtzentrum.",
  "In der Nacht schlief sie wegen Kopfschmerzen schlecht.",
  "Am letzten Wochenende blieb ich zu Hause.",
  "Er griff in die Tasche seiner Jacke.",
  "Gestern Abend saß ich mit meiner Freundin sehr lange Zeit im Cafe.",
  "Es war 2014. Ich sah sie wieder im Urlaub.",
  "Ich dachte immer nur an sie.",
]

def test_verb_tempus_prätertum():
  sentences = verb_tempus_prätertum_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_tempus_prätertum"]})
  display(sentences, nlp)

verb_tempus_präsens_sentences = [
  "Heute ist Sonntag.",
  "Lisa schläft bis zehn Uhr. ",
  "Sie macht ein gutes Frühstück.",
  "Lisa isst nicht gern allein.",
  "Ihr Freund Lukas ist auch da.",
  "Lisa erzählt von der Schule,",
  "Und Lukas spricht über seine Arbeit.",
  "Am Nachmittag trifft Lisa eine Freundin.",
  "Lukas fährt dann nach Hause.",
  "Nach dem Abendessen liest er Bücher.",
]

def test_verb_tempus_präsens():
  sentences = verb_tempus_präsens_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_tempus_präsens"]})
  display(sentences, nlp)

verb_tempus_futur_1_sentences = [
  "Irena wird ein Praktikum machen.",
  "Nora wird ihren Vater besuchen.",
  "Ich werde nicht mehr rauchen.",
  "Die Kinder werden manchmal ihr Zimmer selbt aufräumen.",
]

def test_verb_tempus_futur_1():
  sentences = verb_tempus_futur_1_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_tempus_futur_1"]})
  display(sentences, nlp)

verb_tempus_plusquaperfekt_sentences = [
  "Ich hatte am Abend die Koffer gepackt.",
  "Er rannte zum Zug, aber der Zug war schon abgefahren.",
  "Als wir zur Party kamen, waren die anderen Gäste schon nach Hause gegangen.",
]

def test_verb_tempus_plusquaperfekt():
  sentences = verb_tempus_plusquaperfekt_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_tempus_plusquaperfekt"]})
  display(sentences, nlp)

verb_modus_imperativ_sentences = [
  "Schreib dir das Wort doch mal auf.",
  "Tu doch bitte nicht so, als ob du es nicht gewusst hättest.",
  "Sei so gut und sprich etwas lauter!",
  "Lass das Gerät eben doch reparieren.",
  "Bestellen Sie für mich bitte einen Platz, Herr Meier.",
  "Entschuldige bitte die Störung.",
  "Vergiss nicht, vor der Reise ins Ausland dein Visum zu beantragen.",
  "Hilf deinem Kollegen bei der Arbeit.",
  "Fahr zur Frankfurter Automesse!",
  "Ruhe, Kinder! Seid doch ruhig.",
]

def test_verb_modus_imperativ():
  sentences = verb_modus_imperativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_modus_imperativ"]})
  display(sentences, nlp)

verb_modus_konjunktiv_1_sentences = [
  "Ein Sprecher der Opposition meinte, die Wirtschaftspolitik müsse sofort geändert werden. Das sei unbedingt notwendig.",
  "Der Arzt sagte, ich müsse auch noch die Lungen untersuchen lassen.",
  "Er behauptete, dass er das Staatsexamen gut gemacht habe.",
  "Die Fachleute sind der Meinung, dass die Erfindung das gesamte Verkehrssystem revolutionieren werde.",
  "- Kann er denn Auto fahren? - Er behauptet, er könne Auto fahren.",
]

def test_verb_modus_konjunktiv_1():
  sentences = verb_modus_konjunktiv_1_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_modus_konjunktiv_1"]})
  display(sentences, nlp)

verb_modus_konjunktiv_2_sentences = [
  "Wenn der Zug keine Verspätung gehabt hätte, wäre ich schon in Berlin angekommen.",
  "- Kommst du mit ins Kino? - Ich würde gerne mit euch kommen, aber ich muss noch arbeiten.",
  "Sie wollen in der Volkshochschule Deutsch lernen. Dürfte ich fragen, warum Sie gerade Deutsch lernen wollen?",
  "Wirklich schade! Ich wäre gestern gerne dabei gewesen.",
  "Er war nicht taub. Aber er tat so, als wäre er taub.",
  "- Möchten Sie einen Kaffee? - Ehrlich gesagt, mir wäre eine Tasse Tee lieber.",
  "Monika wollte heute kommen, aber sie ist noch nicht da. Wenn sie bloß käme!",
  "Ich würde Ihnen helfen, wenn ich könnte.",
  "Sehr schön sieht das aus! Ich würde mir das natürlich gerne kaufen, aber mir fehlt im Moment das Geld dazu.",
  "Am besten wäre ich zu Hause geblieben, aber ich musste leider hingehen.",
  "Sie können hier Weiterarbeiten. Wenn das ginge, wäre ich froh.",
  "Hättest du nicht so viel für diesen gebrauchten Wagen verlangt, wäre er schon längst verkauft!",
  " - Ich habe Halsweh. - Du solltest viel Tee trinken.",
  "Zwei Männer machten in München auf Polizisten den Eindruck, als stünden sie unter dem Einfluss von Drogen.",
  "Hättest du mich gestern darum gebeten, hätte ich dir gerne geholfen.",
]

def test_verb_modus_konjunktiv_2():
  sentences = verb_modus_konjunktiv_2_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_modus_konjunktiv_2"]})
  display(sentences, nlp)


verb_genus_passiv_sentences = [
  "- Hat Professor Schulz Sie geprüft? - Ja, von ihm bin ich geprüft worden.",
  "Das Zimmer soll von meiner Frau aufgeräumt werden.",
  "Vergessen Sie nicht, dass vor der Reise ins Ausland das Visum beantragt werden muss!",
  "Bei uns wird am Wochenende nicht gearbeitet.",
  "Parkverbot bedeutet Hier darf nicht geparkt werden.",
  "Die Autofahrer werden gebeten, die Autobahn erst ab Stuckenborstel zu benutzen.",
  "Die Busfahrt hat uns nicht gefallen, weil unterwegs nicht geraucht werden durfte.",
  "Zum Text sind schon einige Fragen gestellt worden.",
  "Ich weiß nicht, ob das Problem schon hat gelöst werden müssen.",
  "Er behauptet, niemals vorher gefragt worden zu sein.",
  "Die alte.Frau ist schwer krank, sie muss sofort ins Krankenhaus gebracht werden.",
  "Der Bedarf an Arbeitskräften muss bald gedeckt werden.",
  "Endlich wurde dieser Vertrag abgeschlossen.",
  "Die Straßen sind von den Bauarbeitern gebaut worden.",
  "- Wer kann den Plan erfüllen? Welcher Passivsatz ist richtig? - Von wem kann der Plan erfüllt werden?",
  "Die inneren Angelegenheiten eines Landes dürfen nicht eingemischt werden.",
  "Das Auto muss auf die Qualität geprüft werden.",
  "Das Fernsehgerät ist kaputt. Es muss sofort repariert werden.",
  "Die Arbeitsbedingungen in der Fabrik werden durch technische Erneuerung verbessert.",
  "Wo kann der Pass ausgestellt werden?",
]

def test_verb_genus_passiv():
  sentences = verb_genus_passiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_genus_passiv"]})
  display(sentences, nlp)

verb_trennbare_sentences = [
  "Die Gäste sind sehr spät angekommen.",
  "Haben die Zeitungen diese wichtige Nachricht veröffentlicht?",
  "Peter hat die Prüfung bestanden, er ist nicht durchgefallen.",
  "Ihr habt das Zimmer noch nicht aufgesetzt.",
  "Wir haben das Fenster schon aufgegeben.",
  "Jan hat den Kindern Märchen vorgelesen.",
  "Kann ich auf dieser Bank ein Konto anfangen?",
  "Ich lerne Tag und Nacht, denn ich muss nächste Woche eine Prüfung ablegen.",
  "Die Firma hat ihn zum 1. Juni entlassen. Dann hat ihn die andere Firma wieder eingestellt.",
  "Die Regierung hat entscheidet, dass neue Arbeitsplätze geschaffen werden müssen.",
]

def test_verb_trennbare():
  sentences = verb_trennbare_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_trennbare"]})
  display(sentences, nlp)

verb_untrennbare_sentences = [
  "Er hat sein Studium 2013 mit dem Staatsexamen abgeschlossen.",
  "Nach bestandener Prüfung warf er seine Bücher aus dem Fenster.",
  "Der Kaffee ist kalt. Du musst den Ober rufen und dich berichten.",
  "Die Bedingungen im Berufsverkehr werden in der Stadt durch langfristige Planung vermehrt.",
  "Wenn er angegriffen wird, muss er sich verteidigen.",
  "Die Luft erhält Sauerstoff.",
  "Wir haben darüber lange gesprochen und uns schließlich für Ihren Vorschlag entschieden.",
  "- Fährt der Zug bis München? - Nein, Sie müssen zweimal umsteigen.",
  "Was hast du denn im letzten Test für eine Note bekommen?",
  "Viele Länder müssen aus dem Ausland Autos einführen.",
]

def test_verb_untrennbare():
  sentences = verb_untrennbare_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_untrennbare"]})
  display(sentences, nlp)

verb_modal_sentences = [
  "Die Regierung hat entschieden, dass neue Arbeitsplätze geschaffen werden müssen.",
  "Der Chef hat gesagt, du sollst zu ihm kommen.",
  "Du darfst Ursula auf keinen Fall etwas verraten, ich will sie überraschen.",
  "- Habt ihr schon Tickets? - Nein, wir müssen noch welche besorgen.",
  "Eigentlich wollte ich schon früh aufbrechen, aber dann bin ich doch noch bis zum Abend bei meiner Schwester geblieben.",
  "- Hast du gestern Nacht besser schlafen können? - Ja, ich habe eine Schlaftablette genommen.",
  "Das Kind ist schwer verletzt, es muss sofort ins Krankenhaus gebracht werden.",
  "Peter hat heute viel Arbeit. Er kann leider nicht kommen.",
  "Hier darfst du nicht hineingehen! Da ist doch ein Schild: 'KEIN EINGANG!'",
  "Ich möchte einen Tee bitte.",
]

def test_verb_modal():
  sentences = verb_modal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_modal"]})
  display(sentences, nlp)


verb_reflexive_sentences = [
  "Kann ich in Jeans zu einer Party gehen, oder muss ich mich umziehen?",
  "Dieser Film war schlecht! Du kannst es dir nicht vorstellen!",
  "Wo habt ihr euch kennen gelernt?",
  "Gisela hat in Mathematik eine Eins bekommen. Darüber hat sie sich selbst am meisten gewundert.",
  "Das Thema interessiert mich, aber ich weiß leider zu wenig davon.",
  "Die Bevölkerung sollte sich umweltfreundlicher verhalten.",
  "Im letzten Jahr hat er sich keine Reise leisten können.",
  "Er ist sehr nett, ich unterhalte mich gern mit ihm.",
  "Was? Du willst heiraten？Überleg dir das gut!",
  "Tina hat eine Einladung bekommen. Sie freut sich sehr.",
]

def test_verb_reflexive():
  sentences = verb_reflexive_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_reflexive"]})
  display(sentences, nlp)

ergänzungen_common = [
  "Diese Bluse ist mir zu eng. Kann ich sie umtauschen?",
  "Ich habe die Kinder zum Arzt gebracht. Was fehlt ihnen denn?",
  "Die Universität hat ihn zum Studium zugelassen.",
  "Endlich haben beide Firmen einen Vertrag abgeschlossen.",
  "Heute hat der Chef ein Gespräch mit den Gästen aus Japan geführt.",
  "Aber schließlich erteilte er der Bank den Auftrag, das Geld an mich auszuzahlen.",
  "Wer möchte noch eine Frage stellen?",
  "Wer hat gestern den Vortrag gehalten?",
  "Sie hat mir ihren Freund vorgestellt.",
  "Bitte, nehmen Sie noch ein Stück Kuchen!",
  "Er hat mir seinen Plan genau erklärt.",
  "Sie ähnelt ihrer Mutter sehr.",
  "Der Chef vertraut seiner Sekretärin sehr.",
  "Der Lärm schadet der Gesundheit der Menschen.",
  "Ich habe ihm das Buch geschenkt.",
  "Wir gedenken der Soldaten, die im Krieg gefallen sind.",
  "Die Fahrt zur Arbeit kostet mich zwei Stunden.",
  "Die Polizei entzog dem Fahrer den Führerschein.",
  "Der Arzt verschrieb dem Patienten das Medikament.",
  "Die traurige Geschichte hat uns tief ergriffen.",
]

verb_ergänzungen_im_akkusativ_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_im_akkusativ():
  sentences = verb_ergänzungen_im_akkusativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_im_akkusativ"]})
  display(sentences, nlp)


verb_ergänzungen_im_dativ_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_im_dativ():
  sentences = verb_ergänzungen_im_dativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_im_dativ"]})
  display(sentences, nlp)

verb_ergänzungen_im_dativ_akkusativ_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_im_dativ_akkusativ():
  sentences = verb_ergänzungen_im_dativ_akkusativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_im_dativ_akkusativ"]})
  display(sentences, nlp)

verb_ergänzungen_im_akkusativ_akkusativ_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_im_akkusativ_akkusativ():
  sentences = verb_ergänzungen_im_akkusativ_akkusativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_im_akkusativ_akkusativ"]})
  display(sentences, nlp)


verb_ergänzungen_im_genitiv_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_im_genitiv():
  sentences = verb_ergänzungen_im_genitiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_im_genitiv"]})
  display(sentences, nlp)

verb_ergänzungen_mit_präposition_sentences = ergänzungen_common + [
]

def test_verb_ergänzungen_mit_präposition():
  sentences = verb_ergänzungen_mit_präposition_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_ergänzungen_mit_präposition"]})
  display(sentences, nlp)

verb_zu_infinitiv_sentences = [
  "Warum benutzen Sie nicht die Gelegenheit, auch Hamburg kennen zu lernen?",
  "Viele Leute treiben Sport, um fit zu bleiben.",
  "Ich habe Grippetabletten genommen, um das Fieber loszuwerden.",
  "Der Krach von Straßenbauarbeiten ist nicht auszuhalten.",
  "Walter hat keine Lust nützukommen.",
  "Ich hoffe, im Sommer nach Deutschland fahren zu können.",
  "Frau Müller hat eine Putzfrau. Sie braucht die Wohung nicht selbst sauberzumachen.",
  "Alter hat heute noch viel zu tun.",
  "Ich habe vergessen, Natalie anzurufen.",
  "Es ist mir wichtig, dich zu treffen.",
]

def test_verb_zu_infinitiv():
  sentences = verb_zu_infinitiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_zu_infinitiv"]})
  display(sentences, nlp)

partizip_common = [
  "Nach bestandener Prüfung warf er seine Bücher aus dem Fenster.",
  "Bei dieser Firma brauchst du dich gar nicht zu bewerben, die nimmt nur Leute mit abgeschlossener Ausbildung.",
  "Die Fallschirme öffneten sich nacheinander, sobald die Soldaten aus dem fliegenden Flugzeug gesprungen waren.",
  "Der Verletzte war nur zu retten, indem er sofort operiert wurde.",
  "Die von mir bestellten Bücher sind heute angekommen.",
  "Seine Leistlung ist überraschend.",
  "Das Fenster ist geöffnet.",
  "Die Kinder gingen gestern lachend ins Kino.",
  "Diese Firma hat mir einen Vertrag unterzeichnet geschickt.",
  "Die Studenten haben die anzuerkennende Leistung vollgebracht.",
]

verb_partizip_1_sentences = partizip_common + [
  "Sie kommt weinend nach Hause.",
  "Der Film ist spannend.",
  "Die Europareise ist anstrengend.",
  "Der zunehmende Verkehr ist ein großes Problem.",
  "Die nach Bonn fahrende Zug  hatte Verspätung.",
  "Die Reisende kommt aus Deutschland.",
]

def test_verb_partizip_1():
  sentences = verb_partizip_1_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_partizip_1"]})
  display(sentences, nlp)

verb_partizip_2_sentences =  partizip_common + [
  "Sie schauten sich das Fußballspiel gespannt an.",
  "Der Fenster ist geöffnet.",
  "Der Platz ist besetzt.", 
  "Der angekommene Zug hat eine halbe Stunde Verspätung.", 
  "Das ins Chinesische übersetzte Buch ist gut.",
  "Der Angestellte hat viel Arbeit zu tun.",
]

def test_verb_partizip_2():
  sentences = verb_partizip_2_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_partizip_2"]})
  display(sentences, nlp)

verb_funktionsverbgefüge_sentences = [
  "Die Personalabteilung hat ihn zur Kenntnis genommen.",
  "Das neue Gesetz ist schon in Kraft getreten.",
  "Beim Deutschlenen hat sie mir Hilfe geleistet.",
  "Auf der Abschiedsparty habe ich von meinen Kollegen Abschied genommen.",
  "Bei der Betriebsratssitzung erhebt ein Mitglied einen Anspruch auf Erhöhung des Lohns.",
  "Wir bringen unseren besten Dank für Ihre Hilfe zum Ausdruck.",
  "Die öffentlichen Verkehrsmittel stehen allen Leuten zur Verfügung.",
  "Dieser Film hat im Festival Anerkennung gefunden.",
  "Dieses Buch hat einen tiefen Eindruck auf die Leser gemacht.",
  "Vor der Reise hat sie das Zimmer in Ordnung gebracht.",
  "Dieser Studienbewerber stellte einen Antrag auf die Zulassung zum Studium.",
  "Der Chef hat ihm einen Auftrag erteilt.",
  "1933 ist Hitler zur Macht gelangt.",
  "Das Theater brachte das Stück zur Aufführung.",
  "Das Semester geht bald zu Ende.",
  "Deutschland hat die diplomatischen Beziehungen zu/mit einem neuen Land aufgenommen.",
  "Die Techniker und die Arbeitnehmer haben zusammen die neu entwickelte Maschine in Betrieb genommen.",
  "Lass mich bitte in Ruhe!",
  "Diese Firma hat eine Vereinbarung mit ihrer Vertretung getroffen.",
  "Die Polizei stellte den Diebstahl unter Strafe.",
]

def test_verb_funktionsverbgefüge():
  sentences = verb_funktionsverbgefüge_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_funktionsverbgefüge"]})
  display(sentences, nlp)

verb_nominalisierung_sentences = [
  "Er betreut den Abbruch seines Studiums.",
  "Sie braucht immer viel Zeit für die Korrektur der Aufsätze.",
  "Wir erwarten die Ankunft des Zuges.",
]

def test_verb_nominalisierung():
  sentences = verb_nominalisierung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_nominalisierung"]})
  display(sentences, nlp)

def test_verb():
  sentences = verb_tempus_perfekt_sentences + verb_tempus_prätertum_sentences + verb_tempus_präsens_sentences + verb_tempus_futur_1_sentences + verb_tempus_plusquaperfekt_sentences
  sentences = sentences + verb_modus_imperativ_sentences + verb_modus_konjunktiv_1_sentences + verb_modus_konjunktiv_2_sentences + verb_genus_passiv_sentences
  sentences = sentences + verb_trennbare_sentences + verb_untrennbare_sentences + verb_modal_sentences + verb_reflexive_sentences
  sentences = sentences + verb_ergänzungen_im_akkusativ_sentences + verb_ergänzungen_im_dativ_sentences + verb_ergänzungen_im_dativ_akkusativ_sentences + verb_ergänzungen_im_genitiv_sentences
  sentences = sentences + verb_ergänzungen_mit_präposition_sentences + verb_zu_infinitiv_sentences + verb_partizip_1_sentences + verb_partizip_2_sentences
  sentences = sentences + verb_funktionsverbgefüge_sentences + verb_nominalisierung_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["VERB"]})
  display(sentences, nlp)


