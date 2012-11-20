class GenericApplication(object):
    def __init__(self):
        object.__init__(self)

    def _initialize(self):
        pass

    def _finalize(self):
        pass

    def _best_fitness(self):
        pass

    def _select(self):
        pass

    def _crossover(self, chromosomes):
        pass

    def _mutation(self, chromosomes):
        pass

    def _update_next_population(self, chromosomes):
        pass

    def run(self, delta=0.01, epoch_number=1000000):
        epoch = 1
        self._initialize()

        while self._best_fitness() > delta and epoch <= epoch_number:
            parental_chromosomes = self._select()

            if chromosomes:
                mutated_chromosomes = self._mutation(chromosomes)

                self._update_next_population(mutated_chromosomes)

            epoch += 1

