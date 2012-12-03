class GenericApplication(object):

    def __init__(self):
        object.__init__(self)

    def _initialize(self):
        pass

    def _finalize(self):
        pass

    def _running(self):
        return False

    def _select(self):
        return None

    def _crossover(self, chromosomes):
        return None

    def _mutation(self, chromosomes):
        pass

    def _update_next_population(self, chromosomes):
        pass

    def run(self):
        self._initialize()

        while self._running():
            parental_chromosomes = self._select()

            chromosomes = self._crossover(parental_chromosomes)

            if chromosomes:
                mutated_chromosomes = self._mutation(chromosomes)

                self._update_next_population(mutated_chromosomes)

        self._finalize()

