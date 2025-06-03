import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        anno = self._view._ddAnno.value
        if anno is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Attenzione selezionare anno!", color = "red"))
            self._view.update_page()
            return

        self._model.buildGraph(int(anno))
        nNodes, nEdges = self._model.getGraphDetails()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con {nNodes} nodi e {nEdges} archi!", color = "blue"))
        self._view.update_page()


    def handleDettagli(self, e):
        if self._selectedTeam is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Attenzione selezionare un team!", color="red"))
            self._view.update_page()
            return

        viciniSorted = self._model.getNeighborsSorted(self._selectedTeam)
        self._view._txt_result.controls.clear()
        for v in viciniSorted:
            self._view._txt_result.controls.append(ft.Text(f"{v[0]} - {v[1]}"))

        self._view.update_page()


    def handlePercorso(self, e):
        if self._selectedTeam is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Attenzione selezionare un team!", color="red"))
            self._view.update_page()
            return

        path, score = self._model.getBestPathV2(self._selectedTeam)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"trovato un cammino che parte da {self._selectedTeam} con somma dei pesi uguale a {score}."))

        for v in path:
            self._view._txt_result.controls.append(ft.Text(f"{v[0]} -- peso: {v[1]}"))

        self._view.update_page()




    def handleDDYearSelection(self, e):
        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(teams)} squadre che hanno giocato nel {self._view._ddAnno.value}"))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = t, text= t.teamCode, on_click=self.readDDTeams))

        self._view.update_page()

    def fillDDYear(self):
        years = self._model.getYears()
        yearsDD = map(lambda x: ft.dropdown.Option(x), years)
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self._selectedTeam = None
        else:
            self._selectedTeam  = e.control.data
        print(f"Selected team: {self._selectedTeam}")
