from service import Service
import libsumo
import os

class GeneticAlgorithm():

    def __init__(self, gui_active : bool, sumo_folder : str, sumo_cfg_file : str) -> None:
        self.gui = gui_active
        self.sumo_folder = sumo_folder
        self.sumo_cfg = sumo_cfg_file

        self.population = []
        
        self.srv = Service(sumo_folder)
    
    def _compute_fitness(self, chromosom : list[float]) -> float:
        pass

    def _select_parents(self) -> list[list[float]]:
        pass

    def _crossing(self) -> list[float]:
        pass
        

    def run(self) -> None:
        conf_file_path = os.path.join(self.sumo_folder, self.sumo_cfg)
        self.srv.generate_rou_file()

        if self.gui:
            libsumo.start(["sumo-gui", "-c", conf_file_path])
        else:
            libsumo.start(["sumo", "-c", conf_file_path])
