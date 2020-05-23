import unittest
import clima_test
import climabuilder_test
import pronostico_test
import sistema_test

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(clima_test.ClimaUnitTests))
    suite.addTest(unittest.makeSuite(climabuilder_test.ClimaBuilderUnitTests))
    suite.addTest(unittest.makeSuite(pronostico_test.PronosticoUnitTests))
    suite.addTest(unittest.makeSuite(sistema_test.SistemaTests))

    unittest.TextTestRunner(verbosity=3).run(suite)

