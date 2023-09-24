import apache_beam as beam

with beam.Pipeline() as pipeline:
  (pipeline
   | 'ReadCSV' >> beam.io.ReadFromText('gs://my-bucket1123/jyostna-tcs_2023-09-17_export.csv')
   | 'WriteToBigQuery' >> beam.io.WriteToBigQuery('qwiklabs-gcp-04-f327abd93d20:asddd.Splitwise'))

pipeline.run()
