from dataset_painter import SeedlingDataset

INPUT_FOLDER = './plantulas_soja/cultivar_2_azul'
OUTPUT_FOLDER = './dataset/plantulas_soja/cultivar_2_azul'

if __name__ == '__main__':
    sd = SeedlingDataset(INPUT_FOLDER, OUTPUT_FOLDER)
    sd.run()
